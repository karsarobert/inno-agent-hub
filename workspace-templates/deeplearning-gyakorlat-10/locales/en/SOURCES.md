# Sources and data version

Teacher demonstrations: PTE_DL10_CAM.ipynb and PTE_DL10_AGE_PRED.ipynb. This task uses new sample images and a new custom split. The original notebooks are not modified or redistributed as student solutions.

The CSV/ZIP use the public Drive identifiers from the supplied age notebook; complete SHA-256 hashes pin both versions. The 239 MB image archive is not bundled. The source CSV has 7591 rows with file_name/real_age columns. The ZIP is a flat numbered image folder, without original train/valid/test or person-identity metadata. We did not establish the original APPA-REAL mapping; the custom 60/20/20 split is not benchmark reproduction. real_age is the source-provided label, not an individually verified age.

Samples: the elephant image is the public image linked by the Keras Grad-CAM example; the sunflower image comes from TensorFlow’s example-image repository. Original sample files and public ImageNet class-index JSON are bundled in assets with source identifiers. Filenames are not verified reference classes.

- [CAM paper](https://arxiv.org/abs/1512.04150)
- [Keras Grad-CAM example](https://keras.io/examples/vision/grad_cam/)
- [ResNet50 model and preprocessing](https://keras.io/api/applications/resnet/resnet_models/)
- [Transfer learning](https://keras.io/guides/transfer_learning/)
- [MAE](https://keras.io/api/losses/regression_losses/)
- [APPA-REAL official description](https://chalearnlap.cvc.uab.es/dataset/26/description/)
- [Elephant source](https://i.imgur.com/Bvro0YD.png)
- [Sunflower source](https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg)
- [ImageNet labels](https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json)

2026-11-15.
