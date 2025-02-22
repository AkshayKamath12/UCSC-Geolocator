import torch
from geoclip import GeoCLIP, train
from geoclip.train import eval_images
import torch.nn as nn
import os
import pandas as pd

def load_gps_data(csv_file):
    data = pd.read_csv(csv_file)
    lat_lon = data[['LAT', 'LON']]
    gps_tensor = torch.tensor(lat_lon.values, dtype=torch.float32)
    return gps_tensor


class Geolocator:
    def __init__(self, use_trained=False, queue_size=4096):
        self.model = GeoCLIP(queue_size=queue_size)
        # self.device = "cpu"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        if use_trained:
            self.load_weights()
            self.model.gps_gallery = load_gps_data(os.path.join(os.getcwd(), "weights/coords.csv"))

    def predict(self, image_path, top_k=1):
        return self.model.predict(image_path, top_k=top_k)

    def train(self, train_dataloader, epoch, batch_size, scheduler=None, criterion=nn.CrossEntropyLoss()):
        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.0001)
        train(train_dataloader, self.model, optimizer, epoch, batch_size, self.device, scheduler=scheduler, criterion=criterion)

    # def test(self, val_dataloader):
    #     return eval_images(val_dataloader, self.model, self.device)

    #load weights from specified files below
    def load_weights(self):
        self.model.image_encoder.mlp.load_state_dict(torch.load("weights/image_encoder_mlp_weights.pth", map_location=torch.device("cpu")))
        self.model.location_encoder.load_state_dict(torch.load("weights/location_encoder_weights.pth", map_location=torch.device("cpu")))
        self.model.logit_scale = nn.Parameter(torch.load("weights/logit_scale_weights.pth", map_location=torch.device("cpu")))

    #save weights to the specified files below
    def save_weights(self):
        torch.save(self.model.image_encoder.mlp.state_dict(), "weights/image_encoder_mlp_weights.pth")
        torch.save(self.model.location_encoder.state_dict(), "weights/location_encoder_weights.pth")
        torch.save(self.model.logit_scale, "weights/logit_scale_weights.pth")