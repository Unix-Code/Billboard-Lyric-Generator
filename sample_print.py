from os import listdir
from os.path import join
import subprocess
import time

def get_checkpoint_nums(checkpoint_path):
    nums = [int(f.split("model.ckpt-")[1].split(".")[0]) for f in listdir(checkpoint_path) if "model.ckpt-" in f]
    nums = list(set(nums))
    return nums

def run(path, tf_path, prime):
    num = -1
    while True:
        new_num = max(get_checkpoint_nums(path))
        if (new_num == num):
            time.sleep(5)
        else:
            num = new_num
            
            out = r'.\test samples\model_{}.txt'.format(num)
            print(out)
            #cmd = 'py sample.py --prime "{}" -q > "{}"'.format(prime, out)
            #print(cmd)
            #p = subprocess.Popen(cmd)

            cmd = ['py', r'C:\Users\David\Documents\GitHub\Billboard-Lyric-Generator\word-rnn-tensorflow\sample.py', '--prime', prime, '--save_dir', r'C:\Users\David\Documents\GitHub\Billboard-Lyric-Generator\word-rnn-tensorflow\save', '-n', '500', '-q']
            print(cmd)
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

            lines = []
            print("Sample Output From Model At Cycle: {}".format(num))
            for line in p.stdout:
                lines.append(line)
                print(line)
                
            while p.poll() is None:
                print("waiting")
                
            print("\n")
            
            with open(out, "w") as f:
                for line in lines:
                    text = str(line.decode('windows-1252'))
                    f.write(text)

            print("Wrote File\n")

if __name__ == "__main__":
    checkpoint_path = r'.\word-rnn-tensorflow\save'
    tf_path = r'.\word-rnn-tensorflow'
    prime = "she"
    
    run(checkpoint_path, tf_path, prime)
