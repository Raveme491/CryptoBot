import torch
from torch import nn

class ModelLstm(nn.Module):
  def __init__(self, input_size, num_hidden, num_layers) -> None:
    super().__init__()

    self.input_size = input_size
    self.num_hidden = num_hidden
    self.num_layers = num_layers

    self.lstm = nn.LSTM(input_size, 
                        num_hidden, 
                        num_layers,
                        batch_first=True,
                        bidirectional=True)

    self.out = nn.Linear(num_hidden,1)

  def forward(self, x):
    self.lstm.flatten_parameters()

    _, (hidden,_) = self.lstm(x)
    o = self.out(hidden[-1])

    return o

net = ModelLstm(input_size = 4, 
                num_hidden = 128, 
                num_layers = 2)
lossfun = nn.MSELoss()
optimizer = torch.optim.AdamW(net.parameters(), lr=.01)
net.load_state_dict(torch.load(r'BotFin/trainedModel.pt'))
