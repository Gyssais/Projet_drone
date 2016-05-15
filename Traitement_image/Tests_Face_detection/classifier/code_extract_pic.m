clc
clear
close all
 
% 创建视频读取对象，并设置参数
xyloObj = VideoReader('video_neg3.mp4'); % 3547帧
 
nFrames = 30*36;
vidHeight = xyloObj.Height;
vidWidth = xyloObj.Width;
FrameRate = xyloObj.FrameRate; % 29帧播放的

% 创建几帧数据的空间
A=nFrames/30;
A=fix(A);
frames = 1:nFrames;
mov(1:length(frames)) = struct('cdata', zeros(vidHeight, vidWidth, 3, 'uint8'), 'colormap', []);
 
% read data
for k = 1 : nFrames
    i=3*k;
    mov(i).cdata = read(xyloObj, frames(i));
    str=strcat('neg4-',int2str(k),'.jpg');
    imwrite(mov(i).cdata(:,:,:),str);
end
 
