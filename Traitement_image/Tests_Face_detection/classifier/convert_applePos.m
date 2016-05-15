
%ImgName = extractfield(applePos,'imageFilename');
clc

fid = fopen('image_location.txt','w');
[a,sizeapplePos] = size(positivePommes);

for i = 1:sizeapplePos
   sousPos = positivePommes(:,i);
   imgNameTab = extractfield(sousPos,'imageFilename');
   ObjPositionTab = sousPos.objectBoundingBoxes;
   [ligne,colonne] = size(ObjPositionTab);
   Nb_apple = ligne;
   
   %ecrire le nome d'image
   imgNametxt = char(imgNameTab(1,1));
   [d,imgName,type]=fileparts(imgNametxt);
   chemin = './positive_images/';
   fprintf(fid,chemin);
   fprintf(fid,imgName);
   fprintf(fid,type);
   %ecrire le nombre de pomme
   fprintf(fid,'\t%d\t',Nb_apple);
  
   for j = 1:Nb_apple
           ObjPosition = ObjPositionTab(j,:);
           for x = 1:4
           fprintf(fid,'%d ',ObjPosition(1,x));
           end
           fprintf(fid,'\t');   
   end
    fprintf(fid,'\n');
end
