# Források és adatváltozat

A két oktatói bemutató: PTE_DL10_CAM.ipynb és PTE_DL10_AGE_PRED.ipynb. A feladat új mintaképeket és új saját felosztást használ. Az eredeti notebookokat nem módosítjuk és nem csomagoljuk újra tanulói megoldásként.

A CSV/ZIP a csatolt életkoros notebook nyilvános Drive-azonosítóival érhető el. A kód mindkettő teljes SHA-256 értékét ellenőrzi. A csomag nem tartalmazza a 239 MB-os képarchívumot. A forrás CSV 7591 sort és file_name/real_age oszlopot tartalmaz. A ZIP lapos, sorszámozott képeket tartalmaz, eredeti train/valid/test vagy személyazonosító-metaadat nélkül. A hivatalos APPA-REAL-megfeleltetést nem igazoltuk; a saját 60/20/20-as felosztás nem benchmark-reprodukció. A real_age a forrás által megadott címke, nem a tutor által ellenőrzött egyéni életkor.

Mintaképek: az elefántos kép a Keras Grad-CAM-példájában megadott nyilvános képből; a napraforgós kép a TensorFlow példaképtárából. Az eredeti képfájlok és a nyilvános ImageNet-osztályindex a csomag assets mappájában vannak, forrásazonosítással. A fájlnevek nem igazolt referenciaosztályok.

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
