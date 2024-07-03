import torch
model = torch.hub.load('milesial/Pytorch-UNet', 'unet_carvana', pretrained=True, scale=0.5)
print(torch.cuda.is_available())
print(dir(model))
