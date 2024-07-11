# Credit: CaliOn2

fence_types = ["_inventory", "_post", "_side"]
slab_types = ["", "_top"]
stairs_types = ["", "_inner", "_outer"]
wall_types = ["_inventory", "_post", "_side", "_side_tall"]

print("This Is A Program To assist in generating models for minecraft 'vic dubs it : snowdog generator'")
print("@vik put the 'name' files in their respective directories and modify their directories to point to the proper directories")
print("block options are: ")
print("block")
print("carpet")
print("fence")
print("slab")
print("snow")
print("stairs")
print("wall")
print("don't add the block option in the first input (name) put it in the second (type)")

while True:
    retard_count = open("retard.txt", "a")
    information1 = input("Add The Block Name Here: ")
    informationbloc = input("Add The Block Type Here: ")
    block_types = informationbloc.split()
    information3 = input("Add Path To Textures Here: ")
    for information2 in block_types :
        retard_count.write(information2)
        if information2 != "block" :
            blockstate = open("blockstates/" + information1 + "_" + information2 + ".json", "w")
            blockstate_struct = open("blockstates/name_" + information2 + ".json", "r")
            blockstate.write(blockstate_struct.read().replace("name", information1))
            blockstate.close()
            blockstate_struct.close()
            model_item = open("models/item/" + information1 + "_" + information2 + ".json", "w")
            model_item_struct = open("models/item/name_" + information2 + ".json", "r")
            model_item.write(model_item_struct.read().replace("name", information1))
            model_item.close()
            model_item_struct.close()
            if information2 == "carpet" :
                model_block = open("models/block/" + information1 + "_carpet.json", "w")
                model_block_struct = open("models/block/name_carpet.json", "r")
                model_block.write(model_block_struct.read().replace("dertex", information3))
                model_block.close()
                model_block_struct.close()
            if information2 == "fence" :
                for i in fence_types :
                    model_block = open("models/block/" + information1 + "_fence" + i + ".json", "w")
                    model_block_struct = open("models/block/name_fence" + i + ".json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3))
                    model_block.close()
                    model_block_struct.close()
            if information2 == "slab" :
                for i in slab_types :
                    model_block = open("models/block/" + information1 + "_slab" + i + ".json", "w")
                    model_block_struct = open("models/block/name_slab" + i + ".json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3))
                    model_block.close()
                    model_block_struct.close()
            if information2 == "snow" :
                for i in range(7) :
                    p = (i + 1) * 2
                    model_block = open("models/block/" + information1 + "_snow_height" + str(p) + ".json", "w")
                    model_block_struct = open("models/block/name_snow_height" + str(p) + ".json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3))
                    model_block.close()
                    model_block_struct.close()
            if information2 == "stairs" :
                for i in stairs_types :
                    model_block = open("models/block/" + information1 + "_stairs" + i + ".json", "w")
                    model_block_struct = open("models/block/name_stairs" + i + ".json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3))
                    model_block.close()
                    model_block_struct.close()
            if information2 == "wall" :
                for i in wall_types :
                    model_block = open("models/block/" + information1 + "_wall" + i + ".json", "w")
                    model_block_struct = open("models/block/name_wall" + i + ".json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3))
                    model_block.close()
                    model_block_struct.close()

        else :
            blockstate = open("blockstates/" + information1 + ".json", "w")
            blockstate_struct = open("blockstates/name.json", "r")
            blockstate.write(blockstate_struct.read().replace("name", information1))
            blockstate.close()
            blockstate_struct.close()
            model_block = open("models/block/" + information1 + ".json", "w")
            model_block_struct = open("models/block/name.json", "r")
            model_block.write(model_block_struct.read().replace("dertex", information3))
            model_block.close()
            model_block_struct.close()
            model_item = open("models/item/" + information1 + ".json", "w")
            model_item_struct = open("models/item/name.json", "r")
            model_item.write(model_item_struct.read().replace("name", information1))
            model_item.close()
            model_item_struct.close()
    retard_count.close()
