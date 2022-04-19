
set LOG=logSS2SMD
set PSEUDO=pseudo1SS2SMD
set TRAINSET='voc_cocostyletrain_SeaShips'
set UNLABELSET='voc_cocostyletrain_SMD'
set TESTSET='voc_cocostyletest1283'

@echo %LOG% %PSEUDO% %TRAINSET% %UNLABELSET% %TESTSET%

python detection/train_stg1.py --logdir=./%LOG% --simple_path --config BACKBONE.WEIGHTS=./ImageNet-R50-AlignPadding.npz DATA.BASEDIR=E:/fjj/SeaShips_SMD DATA.TRAIN="(%TRAINSET%,)" DATA.VAL="(%TESTSET%,)" PREPROC.MAX_SIZE=1000 TRAIN.EVAL_PERIOD=10 TRAIN.LR_SCHEDULE=[7500,10000] TRAIN.NUM_GPUS=1 TRAIN.AUGTYPE_LAB=default
python detection/predict.py --evaluate eval_%LOG%.json --load ./%LOG%/model-20000 --visualize --config DATA.BASEDIR=E:\fjj\SeaShips_SMD DATA.TRAIN="(%UNLABELSET%,)" DATA.VAL="(%TESTSET%,)" RPN.ANCHOR_SIZES="(8,16,32)" PREPROC.TEST_SHORT_EDGE_SIZE=600 TEST.FRCNN_NMS_THRESH=0.3 TEST.RESULT_SCORE_THRESH=0.100
python detection/predict.py --predict_unlabeled ./%PSEUDO% --load ./%LOG%/model-20000 --config DATA.BASEDIR=E:\fjj\SeaShips_SMD DATA.TRAIN="(%UNLABELSET%,)" DATA.VAL="(%TESTSET%,)" RPN.ANCHOR_SIZES="(8,16,32)" PREPROC.TEST_SHORT_EDGE_SIZE=600 TEST.FRCNN_NMS_THRESH=0.3 TEST.RESULT_SCORE_THRESH=0.1
python detection/train_stg2.py --logdir=./%LOG%/STAC --simple_path --pseudo_path ./%PSEUDO% --config BACKBONE.WEIGHTS=./ImageNet-R50-AlignPadding.npz DATA.BASEDIR=E:/fjj/SeaShips_SMD DATA.TRAIN="(%TRAINSET%,)" DATA.VAL="(%TESTSET%,)" DATA.UNLABEL="(%UNLABELSET%,)" MODE_MASK=False PREPROC.MAX_SIZE=1000 FRCNN.BATCH_PER_IM=256 TRAIN.EVAL_PERIOD=10 TRAIN.LR_SCHEDULE=[7500,15000,20000] TRAIN.GAMMA=0.3 TRAIN.NUM_GPUS=1 TRAIN.AUGTYPE_LAB=default TRAIN.AUGTYPE=strong TRAIN.CONFIDENCE=0.9 TRAIN.WU=2
cls

set LOG=logSMD2SS
set PSEUDO=pseudoSMD2SS
set TRAINSET='voc_cocostyletrain_SMD'
set UNLABELSET='voc_cocostyletrain_SeaShips'
set TESTSET='voc_cocostyletest1283'
@echo %LOG% %PSEUDO% %TRAINSET% %UNLABELSET% %TESTSET%

python detection/train_stg1.py --logdir=./%LOG% --simple_path --config BACKBONE.WEIGHTS=./ImageNet-R50-AlignPadding.npz DATA.BASEDIR=E:/fjj/SeaShips_SMD DATA.TRAIN="(%TRAINSET%,)" DATA.VAL="(%TESTSET%,)" PREPROC.MAX_SIZE=1000 TRAIN.EVAL_PERIOD=10 TRAIN.LR_SCHEDULE=[7500,10000] TRAIN.NUM_GPUS=1 TRAIN.AUGTYPE_LAB=default
python detection/predict.py --evaluate eval_%LOG%.json --load ./%LOG%/model-20000 --visualize --config DATA.BASEDIR=E:\fjj\SeaShips_SMD DATA.TRAIN="(%UNLABELSET%,)" DATA.VAL="(%TESTSET%,)" RPN.ANCHOR_SIZES="(8,16,32)" PREPROC.TEST_SHORT_EDGE_SIZE=600 TEST.FRCNN_NMS_THRESH=0.3 TEST.RESULT_SCORE_THRESH=0.100
python detection/predict.py --predict_unlabeled ./%PSEUDO% --load ./%LOG%/model-20000 --config DATA.BASEDIR=E:\fjj\SeaShips_SMD DATA.TRAIN="(%UNLABELSET%,)" DATA.VAL="(%TESTSET%,)" RPN.ANCHOR_SIZES="(8,16,32)" PREPROC.TEST_SHORT_EDGE_SIZE=600 TEST.FRCNN_NMS_THRESH=0.3 TEST.RESULT_SCORE_THRESH=0.1
python detection/train_stg2.py --logdir=./%LOG%/STAC --simple_path --pseudo_path ./%PSEUDO% --config BACKBONE.WEIGHTS=./ImageNet-R50-AlignPadding.npz DATA.BASEDIR=E:/fjj/SeaShips_SMD DATA.TRAIN="(%TRAINSET%,)" DATA.VAL="(%TESTSET%,)" DATA.UNLABEL="(%UNLABELSET%,)" MODE_MASK=False PREPROC.MAX_SIZE=1000 FRCNN.BATCH_PER_IM=256 TRAIN.EVAL_PERIOD=10 TRAIN.LR_SCHEDULE=[7500,15000,20000] TRAIN.GAMMA=0.3 TRAIN.NUM_GPUS=1 TRAIN.AUGTYPE_LAB=default TRAIN.AUGTYPE=strong TRAIN.CONFIDENCE=0.9 TRAIN.WU=2
cls

rem --evaluate evaldemo.json --load ../log00/STAC/model-40000 --predict E:\fjj\SeaShips_SMD\JPEGImages\MVI_1592_VIS_00462.jpg --config DATA.BASEDIR=E:\fjj\SeaShips_SMD DATA.TRAIN="('voc_cocostyleunlabel0',)" DATA.VAL="('voc_cocostyletest',)" RPN.ANCHOR_SIZES="(8,16,32)" PREPROC.TEST_SHORT_EDGE_SIZE=600 TEST.FRCNN_NMS_THRESH=0.3 TEST.RESULT_SCORE_THRESH=0.100