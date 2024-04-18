from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_creator import SC2BuildOrderCreator
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB



def main():
    SC2BuildOrderDB.init("build_order")




    build_order_csv = "two_base_blink(error).csv"
    build_order_creator = SC2BuildOrderCreator()
    build_order_creator.create_build("TwoBaseBlink", "Protoss", build_order_csv)

if __name__ == "__main__":
    main()