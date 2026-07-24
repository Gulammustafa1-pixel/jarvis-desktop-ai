from openwakeword.model import Model


model = Model(
    inference_framework="onnx"
)


print("Available wake words:")

for name in model.models.keys():
    print(name)