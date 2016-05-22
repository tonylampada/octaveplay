Toy project to play with octave and other things.

Install docker and build the image with `./build.sh` (go grab some coffee. This will tak e a while)
Alternatively you can pull from dockerhub:
```
docker pull tonylampada/octaveplay
docker tag tonylampada/octaveplay octaveplay
```
(Coffee should be needed as well)


Run the image with `./run.sh`
Once inside the image, run `source dksetup.sh` (ignore the authentication failure error) - this will allow you to run GUI applications.

Note: You may need to update the uid and gid in dksetup [according to this](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)

# Test oct2py
Start python and test oct2py

```
import oct2py
oc = oct2py.Oct2Py()
x = oc.zeros(3,3)
print(x, x.dtype)

#expect:
#[[ 0.  0.  0.]
# [ 0.  0.  0.]
# [ 0.  0.  0.]] float64
#...
```


# Test octave

Now let's try to predict some function like 3x²/y - 17xy + 8/z + 0w - 13

octave run.oct

# Test graphic environment

Run octave in interactive mode and plot a sin func:

```
t = [0:0.01:1];
y1 = sin(2*pi*4*t);
plot(t, y1)
```
