import argparse
import logging
import time

import volumeCalculator

def main():
    """Short description of the function

    Detailed Description of this function

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.
    """

    startTime = time.time()
    logging.basicConfig(filename="log/Log[{0}].log".format(int(startTime)),
                        level= logging.DEBUG,
                        format= "[%(levelname)s] %(asctime)s - %(message)s")
    
    
    #Log start time
    logging.getLogger().info("Started at {0}".format(startTime))


    logging.getLogger().info("-------------------Parser Action-----------------------")

    #parser Action

    parser = argparse.ArgumentParser(description="Calcing the Radius of spheres")
    parser.add_argument("radie", metavar="R", type= float, default=[1], nargs='*', help="Radie of the spheres to calulate")
    parser.add_argument("--debug",type=bool, nargs='?', const=True, default=False, help="Wanna debug ?")
    parser.add_argument("--someString", type = str, default="Some default String", help = "Just a string")

    FLAGS, unparsed = parser.parse_known_args()

    for r in FLAGS.radie:
        print(volumeCalculator.calcSphere(r))

    print(FLAGS.debug)

    logging.getLogger().info("-------------------Calcing Action-----------------------")

    #calc smth could now have more logic
    
    print(volumeCalculator.calcSphere(5))
    print(volumeCalculator.calcSphere(0.2))

    print(volumeCalculator.calcSphere(-4))
    print(volumeCalculator.calcSphere("Test"))


    logging.getLogger().info("-------------------All Log Types Action-----------------------")
    #Log all types of Levels
    logging.getLogger().debug("Am i here ?")
    logging.getLogger().info("Next time pls do this")
    logging.getLogger().warning("Some problem occured, but its fine")
    logging.getLogger().error("Types did not match in ...")
    logging.getLogger().critical("ICH BRENNNE")

    logging.getLogger().info("-------------------On Program End-----------------------")
    logging.getLogger().info("[runTime]: %s" % (time.time()-startTime))

if __name__ == "__main__":
    main()