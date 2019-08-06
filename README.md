# Process

 * Step 1: Start by looking at the source of information to find out what I'm dealing with.

 * Step 2: after understanding the problem. Start to think about most efficient solution.

  Thinking about what type of object could be used. **dictionary** ?

* Step 3: Optimize

  Dictionary can’t have a value of non existing key incremented by 1.

  But I don’t want to check for every single package if their key exists.

  Therefore i choose to handle error and add the key if the problem rises.

  At some point package with a lot of occurrence will make me win time.


* Step 4:

  Find existing tool to sort a dictionary properly.

# Logic

First I build the algorithm. [PackageState_first_batch.py](./PackageState_first_batch.py)

Second code it in the main to have something functional that I will implement in a proper way.

**timing** 
```
I reached that state with a functional code around 8:40pm

Then I started to slow down to look for way to achieve better.
```


Adding error handling and function.

I left the download of the file for the end as I have a slow connection and just worked on a samples.

## missing

I also omitted unittest.

With more time I would have written a test for the input argument.
And probably some for the output of the packages parsing

It's also missing come cleanup of the file.

I was thinking about using tmp_file that can be erase after each run

# Usage

`PackateStat.py arm64`

* that will use mylist, I had to modify the file as it was using a bigger file that I can't upload.

  `python3 PackageState_first_batch.py`
