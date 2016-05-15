clc
clear
close all
 
% ������Ƶ��ȡ���󣬲����ò���
xyloObj = VideoReader('video_neg3.mp4'); % 3547֡
 
nFrames = 30*36;
vidHeight = xyloObj.Height;
vidWidth = xyloObj.Width;
FrameRate = xyloObj.FrameRate; % 29֡���ŵ�

% ������֡���ݵĿռ�
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
 
