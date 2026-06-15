// cutout.swift — Apple Vision foreground subject lift -> transparent PNG.
// Same engine as the macOS "press-and-hold to copy subject" feature. macOS 14+.
// usage:  swift cutout.swift <input-image> <output.png>
// Pairs with image2.py: generate a shot, then cut the subject onto transparent
// background for compositing / catalog use (raises automation rate).
import Foundation
import Vision
import CoreImage
import AppKit

let args = CommandLine.arguments
guard args.count >= 3 else {
    FileHandle.standardError.write("usage: swift cutout.swift <input-image> <output.png>\n".data(using: .utf8)!)
    exit(2)
}
let inPath = args[1], outPath = args[2]

guard let img = NSImage(contentsOfFile: inPath),
      let tiff = img.tiffRepresentation,
      let bmp = NSBitmapImageRep(data: tiff),
      let cg = bmp.cgImage else {
    FileHandle.standardError.write("error: cannot load \(inPath)\n".data(using: .utf8)!); exit(1)
}

let handler = VNImageRequestHandler(cgImage: cg, options: [:])
let req = VNGenerateForegroundInstanceMaskRequest()
do { try handler.perform([req]) } catch {
    FileHandle.standardError.write("error: vision failed: \(error)\n".data(using: .utf8)!); exit(1)
}
guard let obs = req.results?.first else {
    FileHandle.standardError.write("error: no foreground subject found\n".data(using: .utf8)!); exit(1)
}

do {
    let pb = try obs.generateMaskedImage(ofInstances: obs.allInstances, from: handler, croppedToInstancesExtent: true)
    let ci = CIImage(cvPixelBuffer: pb)
    let ctx = CIContext()
    guard let out = ctx.createCGImage(ci, from: ci.extent) else { exit(1) }
    let rep = NSBitmapImageRep(cgImage: out)
    guard let data = rep.representation(using: .png, properties: [:]) else { exit(1) }
    try data.write(to: URL(fileURLWithPath: outPath))
    print("wrote \(outPath) [\(out.width)x\(out.height)] (\(obs.allInstances.count) instance(s))")
} catch {
    FileHandle.standardError.write("error: \(error)\n".data(using: .utf8)!); exit(1)
}
