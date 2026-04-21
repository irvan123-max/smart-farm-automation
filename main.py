from farm import SmartFarm
from utils import print_banner
from config import FARM_NAME

def main():
    print_banner()

    farm = SmartFarm("data_produksi.csv", FARM_NAME)
    farm.run()

if __name__ == "__main__":
    main()