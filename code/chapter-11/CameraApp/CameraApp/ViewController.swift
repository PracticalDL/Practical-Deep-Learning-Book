//
//  ViewController.swift
//  CameraApp
//
//  Created by Meher Kasam on 3/18/18.
//  Copyright © 2018 Meher Kasam. All rights reserved.
//

import UIKit
import AVFoundation
import CoreML
import Vision

class ViewController: UIViewController, CameraFrameDelegate {

    @IBOutlet weak var cameraView: UIImageView!
    @IBOutlet weak var cameraInaccessibleLabel: UILabel!
    @IBOutlet weak var predictionsLabel: UILabel!
    private var cameraHelper: CameraHelper?
    private let model: MLModel = Resnet50().model
    private var lastFrameProcessed = Date()

    override func viewDidLoad() {
        super.viewDidLoad()

        self.cameraHelper = CameraHelper(.back)

        // if camera helper returned nil, we could not get access to the camera
        // so display a message about it
        self.cameraInaccessibleLabel.isHidden = (self.cameraHelper != nil)
        self.cameraHelper?.delegate = self
    }

    func frameCaptured(_ frame: UIImage) {
        DispatchQueue.main.async {
            self.cameraView.image = frame
        }

        let currentTime = Date()

        if currentTime.timeIntervalSince(self.lastFrameProcessed) * 1000 < 32 {
            //return
        }

        self.lastFrameProcessed = currentTime

        guard let model = try? VNCoreMLModel(for: self.model) else {
            NSLog("Unable to load ML Model.")
            return
        }

        // track when the request is initiated
        let startTime = Date()

        let classificationRequest = VNCoreMLRequest(model: model) {
            [weak self] (request, _) in
            if let observations = request.results as? [VNClassificationObservation] {
                // get first 2 results from observations array whose confidence value
                // is greater than 2% and join the results by commas
                let results = observations[..<2].filter { $0.confidence > 0.02 }.map { String(format: "\($0.identifier) - %.0f%%", $0.confidence * 100) }.joined(separator: "\n")

                // track when the request is completed
                let endTime = Date()

                // measure difference between the two times
                let timeInterval = endTime.timeIntervalSince(startTime)

                self?.setPredictionsLabel(results, executionTime: timeInterval)
            }
        }

        guard let cgImage = frame.cgImage else { return }

        let requestHandler = VNImageRequestHandler(cgImage: cgImage)
        try? requestHandler.perform([classificationRequest])
    }

    func setPredictionsLabel(_ string: String, executionTime: TimeInterval) {
        DispatchQueue.main.async {
            self.predictionsLabel.text = String(format: "Predictions in %.0f ms:\n%@", executionTime * 1000, string)
        }

        print("\(Int(executionTime * 1000))")
    }
}
