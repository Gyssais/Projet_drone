./opencv_traincascade -data obj-classifier -vec pos-samples.vec -bg neg_img.txt -precalcValBufSize 2048 -precalcIdxBufSize 2048 -numPos 63 -numNeg 1063 -nstages 20 -minhitrate 0.999 -maxfalsealarm 0.5 -w 50 -h 50 -nonsym -baseFormatSave