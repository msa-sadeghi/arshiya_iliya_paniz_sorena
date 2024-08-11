# myfile = open("test.txt", "w")
# print("hello", "every", "body", sep="*", end=" ", file=myfile)
# print("how are you today?", file=myfile)1
import time

message = "hello every body. how are you today?"
for c in message:
    print(c, end="", flush=True)
    time.sleep(0.2)