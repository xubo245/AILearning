## edit gitignore
	 vi .gitignore 

## Solution

	 git rm -r --cached . 
## History
	
	localhost:AILearning xubo$ git status
	On branch master
	Your branch is up to date with 'origin/master'.
	
	Changes to be committed:
	  (use "git reset HEAD <file>..." to unstage)
	
		modified:   .gitignore
		new file:   .idea/AILearning.iml
		new file:   .idea/encodings.xml
		new file:   .idea/misc.xml
		new file:   .idea/modules.xml
		new file:   .idea/vcs.xml
		new file:   .idea/workspace.xml
		new file:   TensorFlowLearning/data/output/tfrecord/0_Label_0.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/10_Label_10.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/11_Label_11.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/12_Label_12.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/13_Label_13.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/14_Label_14.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/15_Label_15.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/16_Label_16.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/17_Label_17.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/18_Label_18.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/19_Label_19.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/1_Label_1.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/2_Label_2.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/3_Label_3.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/4_Label_4.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/5_Label_5.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/6_Label_6.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/7_Label_7.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/8_Label_8.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/9_Label_9.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/train.tfrecords
		new file:   TensorFlowLearning/src/TFrecordTest.py
		new file:   TensorFlowLearning/src/__init__.py
		new file:   TensorFlowLearning/src/tensorflowHelloWorld.py
	
	localhost:AILearning xubo$ git status
	On branch master
	Your branch is up to date with 'origin/master'.
	
	Changes to be committed:
	  (use "git reset HEAD <file>..." to unstage)
	
		modified:   .gitignore
		new file:   .idea/AILearning.iml
		new file:   .idea/encodings.xml
		new file:   .idea/misc.xml
		new file:   .idea/modules.xml
		new file:   .idea/vcs.xml
		new file:   .idea/workspace.xml
		new file:   TensorFlowLearning/data/output/tfrecord/0_Label_0.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/10_Label_10.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/11_Label_11.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/12_Label_12.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/13_Label_13.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/14_Label_14.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/15_Label_15.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/16_Label_16.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/17_Label_17.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/18_Label_18.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/19_Label_19.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/1_Label_1.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/2_Label_2.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/3_Label_3.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/4_Label_4.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/5_Label_5.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/6_Label_6.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/7_Label_7.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/8_Label_8.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/9_Label_9.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/train.tfrecords
		new file:   TensorFlowLearning/src/TFrecordTest.py
		new file:   TensorFlowLearning/src/__init__.py
		new file:   TensorFlowLearning/src/tensorflowHelloWorld.py
	
	localhost:AILearning xubo$   git rm -r --cached . 
	rm '.gitignore'
	rm '.idea/AILearning.iml'
	rm '.idea/encodings.xml'
	rm '.idea/misc.xml'
	rm '.idea/modules.xml'
	rm '.idea/vcs.xml'
	rm '.idea/workspace.xml'
	rm 'LICENSE'
	rm 'TensorFlowLearning/data/output/tfrecord/0_Label_0.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/10_Label_10.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/11_Label_11.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/12_Label_12.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/13_Label_13.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/14_Label_14.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/15_Label_15.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/16_Label_16.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/17_Label_17.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/18_Label_18.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/19_Label_19.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/1_Label_1.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/2_Label_2.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/3_Label_3.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/4_Label_4.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/5_Label_5.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/6_Label_6.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/7_Label_7.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/8_Label_8.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/9_Label_9.jpg'
	rm 'TensorFlowLearning/data/output/tfrecord/train.tfrecords'
	rm 'TensorFlowLearning/src/TFrecordTest.py'
	rm 'TensorFlowLearning/src/__init__.py'
	rm 'TensorFlowLearning/src/tensorflowHelloWorld.py'
	localhost:AILearning xubo$ git add .
	localhost:AILearning xubo$ git status
	On branch master
	Your branch is up to date with 'origin/master'.
	
	Changes to be committed:
	  (use "git reset HEAD <file>..." to unstage)
	
		modified:   .gitignore
		new file:   TensorFlowLearning/data/output/tfrecord/0_Label_0.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/10_Label_10.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/11_Label_11.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/12_Label_12.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/13_Label_13.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/14_Label_14.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/15_Label_15.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/16_Label_16.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/17_Label_17.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/18_Label_18.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/19_Label_19.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/1_Label_1.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/2_Label_2.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/3_Label_3.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/4_Label_4.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/5_Label_5.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/6_Label_6.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/7_Label_7.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/8_Label_8.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/9_Label_9.jpg
		new file:   TensorFlowLearning/data/output/tfrecord/train.tfrecords
		new file:   TensorFlowLearning/src/TFrecordTest.py
		new file:   TensorFlowLearning/src/__init__.py
		new file:   TensorFlowLearning/src/tensorflowHelloWorld.py
	
	localhost:AILearning xubo$ 
