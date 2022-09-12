# Published results of  hannah😋😋

![Hey there, I'm yoyo this is 阿球圓滾滾](阿球圓滾滾.gif)

## Git instruction
* 下載資料（第一次）
	* https://github.com/yuyu-rap/yuyu-rap.git 改成你需要遠專抓取的資料
	```sh
  	$ git clone https://github.com/yuyu-rap/topic.git
  	```
* 在本地端加入檔案
	* 如果不想上傳全部檔案可以把add .改成add filename
	```sh
  	$ git add .
  	```
* 取消git add
	* 如果不想全部取消可以把staged .改成staged filename
	```sh
  	$ git restore --staged .
  	```
* commit 指令
	* example_commit_text改成你想commit的文字
	```sh
  	$ git commit -m "example_commit_text"
  	```
* 查看狀態
	```sh
  	$ git status
  	```
* 下載資料
	```sh
  	$ git pull
  	```
* 上傳資料
	```sh
  	$ git push
  	```
* 查詢所有本地分支
	```sh
  	$ git branch
  	```
* 查詢所有遠端分支
	```sh
  	$ git branch -a
  	```
* 切換到其他分支
	* example_branch改成你要切換的分支名稱
	```sh
  	$ git checkout example_branch
  	```
* 合併其他分支進來
	* example_branch改成你要合併的分支名稱
	```sh
  	$ git merge example_branch
  	```
## Git 常用腳本
* 本地端資料夾上傳至遠端（第一次時使用)
	* https://github.com/yuyu-rap/topic.git 改成你新創git的ssh
		```sh
	  	git init
		git add .
		git commit -m "add new master"
		git remote add origin https://github.com/yuyu-rap/topic.git
		git push -u origin master  
 	  	```
* 上傳更動資料
	* 一鍵上傳
		```sh
	  	git add .
		git commit -m "edit"
		git push
 	  	```
* 回復之前的版本
	* 把817fc1679b8bdf7e9826aa8e50cb15f088103a3a改成你想回覆的版本
	* 把f21dd836e60ae11467dc4ea40ffaf48988ed2b26改成目前的版本
		```sh
	  	git reset --hard 817fc1679b8bdf7e9826aa8e50cb15f088103a3a
		git reset f21dd836e60ae11467dc4ea40ffaf48988ed2b26
		git add .
		git commit -m "recover"
		git push
 	  	```
## report
* [進度簡報](report/2022_05_06.pptx)

## code
* [手腳分開的正確率預測](code/Correct_prediction.py)
* [手腳同時的正確率預測](code/Correct_prediction_foot&hand.py)
* [即時正確率輸出](code/immediate_prediction.ipynb)
* [用CSV轉成圖片](code/csv_to_picture%20.ipynb)
* [讀取csv加上sqrt傅立葉](code/fft_to_csv.ipynb)
* [讀取csv加上arctan傅立葉](code/fft_arctan_to_csv.ipynb)
* [讀取csv加上sqrt和arctan傅立葉](code/fft_sqrt_arctan_to_csv.ipynb)
