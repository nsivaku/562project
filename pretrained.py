import torch
import torch.nn as nn
import clip
from PIL import Image

class YoutubePredictor(nn.Module):
    
    def __init__(self):
        super(YoutubePredictor, self).__init__()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-L/14", device=device)
        encoder_layer = nn.TransformerEncoderLayer(d_model=1027, nhead=8)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=6)
        self.linear = nn.Linear(1027, 1)
        
        
        
    def forward(self, images, texts, previous_video_feats):
        with torch.no_grad():
            image_features = self.model.encode_image(images)
            text_features = self.model.encode_text(texts)
            vid_features = torch.cat((image_features, text_features), dim=1)
            vid_features = torch.cat((previous_video_feats, previous_video_feats), dim=1)
            
        output = self.transformer_encoder(vid_features)
        output = self.linear(output)
        return output

    @torch.no_grad()
    def generate(self, images, texts, previous_video_feats):
        output = self.forward(images, texts, previous_video_feats)
        return output
        

if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-L/14", device=device)

    image = preprocess(Image.open("mrbeast_stop.jpeg")).unsqueeze(0).to(device)
    text = clip.tokenize(["7 Days Stranded On An Island"]).to(device)
    
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
    
    previous_video_feats = torch.tensor([[120693555, 127912, 253]])
    
    yt_model = YoutubePredictor()
    yt_model.to(device)
    
    print(yt_model.generate(image_features, text, previous_video_feats))