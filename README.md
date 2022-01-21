## Download Dataset of Music21 &amp; AudioSet &amp; VGGSound
This repository is aimed to help you get datasets in field of music separation.
* For `Nusic21` Dataset, run `Music21.py`. Downloaded files will be stored in `Dataset/Music21`
  * Files will be named in this foarmat:`YoutubeID`+`+`+`label`+`.mp4`
  
    



* For `AudioSet` Dataset, run `AudioSet.py`. Downloaded files will be stored in `Dataset/AudioSet`
  * Files will be named in this format: `SerialNum`+`YoutubeID`+`.mp4`
  * You may notice that filename does not contain label. Thats because the dataset itself is in a mess. A little  fragment may contain several type of music. To match each video with its `label index`(Starts with a '/' and a letter, for example  "/m/012xff"), refer to [CSV Source File](SourceFile/AudioSet/balanced_train_segments.csv). After you get the `label index`, you have to consult [ontology.json](SourceFile/AudioSet/ontology.json) or [this file](SourceFile/AudioSet/AudioSet.csv) for its real `label`





* For `VGGSound` Dataset, run `VGGSound.py`. Downloaded files will be stored in `Dataset/VGGSound`
  * Files will be named in this format: `SerialNum+`+`label`+`.mp4`



:warning:**The dataset is very very large. For each dataset, if you don't need every record of it, you can download part of it by assign `start` and `end` in each python file**