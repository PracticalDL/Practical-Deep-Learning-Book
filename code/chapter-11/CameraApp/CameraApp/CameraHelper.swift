//
//  CameraHelper.swift
//  CameraApp
//
//  Created by Meher Kasam on 3/18/18.
//  Copyright © 2018 Meher Kasam. All rights reserved.
//

import AVFoundation
import UIKit

protocol CameraFrameDelegate: class {
    func frameCaptured(_ frame: UIImage)
}

class CameraHelper: NSObject, AVCaptureVideoDataOutputSampleBufferDelegate {
    weak var delegate: CameraFrameDelegate?

    private var captureDevice: AVCaptureDevice!
    private var captureSession: AVCaptureSession!
    private var input: AVCaptureDeviceInput!
    private var videoOutput: AVCaptureVideoDataOutput!
    private let queue = DispatchQueue(label: "camera-frames")
    var permissionGrantedForCamera: Bool = false

    private override init() {}

    convenience init?(_ cameraPosition: AVCaptureDevice.Position) {
#if arch(i386) || arch(x86_64)
        // cannot run camera code on simulator
        return nil
#endif

        self.init()
        self.captureSession = AVCaptureSession()
        self.captureSession.sessionPreset = .medium

        switch AVCaptureDevice.authorizationStatus(for: .video) {
        case .authorized:
            self.permissionGrantedForCamera = true
            break
        case .notDetermined:
            AVCaptureDevice.requestAccess(for: .video) { [weak self] granted in
                self?.permissionGrantedForCamera = granted
            }
        default:
            self.permissionGrantedForCamera = false
        }

        guard self.permissionGrantedForCamera else { return nil }

        self.captureDevice = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: cameraPosition)

        do {
            try self.input = AVCaptureDeviceInput(device: self.captureDevice)
        } catch {
            // handle exception here
        }

        if self.captureSession.canAddInput(self.input) {
            self.captureSession.addInput(self.input)
        }

        self.videoOutput = AVCaptureVideoDataOutput()
        self.videoOutput.setSampleBufferDelegate(self, queue: self.queue)

        if self.captureSession.canAddOutput(self.videoOutput) {
            self.captureSession.addOutput(self.videoOutput)
        }

        let connection = self.videoOutput.connection(with: .video)
        connection?.videoOrientation = .portrait
        connection?.isVideoMirrored = false

        self.captureSession.startRunning()
    }

    func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        guard let image = self.imageFromSampleBuffer(buffer: sampleBuffer) else { return }
        self.delegate?.frameCaptured(image)
    }

    func imageFromSampleBuffer(buffer: CMSampleBuffer) -> UIImage? {
        guard let imageBuffer: CVImageBuffer = CMSampleBufferGetImageBuffer(buffer) else { return nil }
        let ciImage = CIImage(cvPixelBuffer: imageBuffer)

        let width = CGFloat(CVPixelBufferGetWidth(imageBuffer))
        let height = CGFloat(CVPixelBufferGetHeight(imageBuffer))
        let imageRect: CGRect = CGRect(x: 0, y: 0, width: width, height: height)
        let ciContext = CIContext.init()
        guard let cgImage = ciContext.createCGImage(ciImage, from: imageRect) else { return nil }

        let image = UIImage(cgImage: cgImage)
        return image
    }
}
