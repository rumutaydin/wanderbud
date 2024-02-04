pytorch file has the best confidence score. 

To increase the performance and lower the complexity,
TensorFlow Lite inference has been used as well as quantization to int8 and fp16.

int8 inference confidence score was really low, so we used fp16 file in raspberry and got around 1 fps from our camera (we didn't use any ML accelerator)

For reference, see the results for the three checkpoint
