import os
if __name__ == '__main__':
        print 'current Process {} start ...'.format(os.getpid())
        pid = os.fork()
        if pid < 0:
                print 'error in fork'
        elif pid == 0:
            print 'child process {}, parent process {}'.format(os.getpid(), os.getppid())
        else:
            print "I {} create child process {}".format(os.getpid(), pid)

