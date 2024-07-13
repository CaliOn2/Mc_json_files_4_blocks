import json
import os

fence_types = ["_inventory", "_post", "_side"]
slab_types = ["", "_top"]
stairs_types = ["", "_inner", "_outer"]
wall_types = ["_inventory", "_post", "_side", "_side_tall"]

print("This Is A Program To assist in generating models for minecraft 'vik dubs it : snowdog generator'")
print("@vik put the 'name' files in their respective directories and modify their directories to point to the proper directories")
print("block options are: ")
print("block")
print("stairs")
print("slab")
print("fence")
print("wall")
print("carpet")
print("snow")
print("don't add the block option in the first input (name) put it in the second (type)")
information4 = input("Your ModId:")

# Ensure the lang directory exists
os.makedirs("lang", exist_ok=True)

# Load existing en_us.json or create an empty dictionary
lang_file_path = "lang/en_us.json"
if os.path.exists(lang_file_path):
    with open(lang_file_path, "r") as lang_file:
        lang_data = json.load(lang_file)
else:
    lang_data = {}

while True:
    information1 = input("Add The Block Name Here: ")
    informationbloc = input("Add The Block Type Here: ")
    block_types = informationbloc.split()
    information3 = input("Add Path To Textures Here: ")
    information5 = input("What block properties to copy (all lower case):")

    registry_file = open("block_registry.txt", "a")

    for information2 in block_types:

        # Add lang entry
        lang_key = f"block.{information4}.{information1}_{information2}"
        lang_value = f"{information1.replace('_', ' ').title()} {information2.replace('_', ' ').title()}"
        lang_data[lang_key] = lang_value

        registry_code = ""

        if information2 != "block":
            blockstate = open(f"blockstates/{information1}_{information2}.json", "w")
            blockstate_struct = open(f"blockstates/name_{information2}.json", "r")
            blockstate.write(blockstate_struct.read().replace("name", information1).replace("modid", information4))
            blockstate.close()
            blockstate_struct.close()

            model_item = open(f"models/item/{information1}_{information2}.json", "w")
            model_item_struct = open(f"models/item/name_{information2}.json", "r")
            model_item.write(model_item_struct.read().replace("name", information1))
            model_item.close()
            model_item_struct.close()

            if information2 == "carpet":
                model_block = open(f"models/block/{information1}_carpet.json", "w")
                model_block_struct = open("models/block/name_carpet.json", "r")
                model_block.write(model_block_struct.read().replace("dertex", information3).replace("modid", information4))
                model_block.close()
                model_block_struct.close()
                registry_code += f'public static final RegistryObject<Block> {information1.upper()}_CARPET = registerBlock("{information1}_carpet", () -> new CarpetBlock(BlockBehaviour.Properties.copy(Blocks.{information5.upper()}).noOcclusion()));'

            if information2 == "fence":
                for i in fence_types:
                    model_block = open(f"models/block/{information1}_fence{i}.json", "w")
                    model_block_struct = open(f"models/block/name_fence{i}.json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3).replace("modid", information4))
                    model_block.close()
                    model_block_struct.close()
                registry_code += registry_code + f'public static final RegistryObject<Block> {information1.upper()}_FENCE = registerBlock("{information1}_fence", () -> new FenceBlock(BlockBehaviour.Properties.copy(Blocks.{information5.upper()}).noOcclusion()));'

            if information2 == "slab":
                for i in slab_types:
                    model_block = open(f"models/block/{information1}_slab{i}.json", "w")
                    model_block_struct = open(f"models/block/name_slab{i}.json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3).replace("modid", information4))
                    model_block.close()
                    model_block_struct.close()
                registry_code += registry_code + f'public static final RegistryObject<Block> {information1.upper()}_SLAB = registerBlock("{information1}_slab", () -> new SlabBlock(BlockBehaviour.Properties.copy(Blocks.{information5.upper()}).noOcclusion()));'

            if information2 == "snow":
                for i in range(7):
                    p = (i + 1) * 2
                    model_block = open(f"models/block/{information1}_snow_height{p}.json", "w")
                    model_block_struct = open(f"models/block/name_snow_height{p}.json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3).replace("modid", information4))
                    model_block.close()
                    model_block_struct.close()
                registry_code += registry_code + f'public static final RegistryObject<Block> {information1.upper()}_SNOW = registerBlock("{information1}_snow", () -> new SnowLayerBlock(BlockBehaviour.Properties.copy(Blocks.{information5.upper()}).noOcclusion()));'

            if information2 == "stairs":
                for i in stairs_types:
                    model_block = open(f"models/block/{information1}_stairs{i}.json", "w")
                    model_block_struct = open(f"models/block/name_stairs{i}.json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3).replace("modid", information4))
                    model_block.close()
                    model_block_struct.close()
                registry_code += registry_code + f'public static final RegistryObject<Block> {information1.upper()}_STAIRS = registerBlock("{information1}_stairs", () -> new StairBlock(() -> BlockRegistry.{information1.upper()}.get().defaultBlockState(), BlockBehaviour.Properties.copy(Blocks.{information5.upper()}).noOcclusion()));'

            if information2 == "wall":
                for i in wall_types:
                    model_block = open(f"models/block/{information1}_wall{i}.json", "w")
                    model_block_struct = open(f"models/block/name_wall{i}.json", "r")
                    model_block.write(model_block_struct.read().replace("dertex", information3).replace("modid", information4))
                    model_block.close()
                    model_block_struct.close()
                registry_code += registry_code + f'public static final RegistryObject<Block> {information1.upper()}_WALL = registerBlock("{information1}_wall", () -> new WallBlock(BlockBehaviour.Properties.copy(Blocks.{information5.upper()}).noOcclusion()));'

        else:
            blockstate = open(f"blockstates/{information1}.json", "w")
            blockstate_struct = open("blockstates/name.json", "r")
            blockstate.write(blockstate_struct.read().replace("name", information1).replace("modid", information4))
            blockstate.close()
            blockstate_struct.close()

            model_block = open(f"models/block/{information1}.json", "w")
            model_block_struct = open("models/block/name.json", "r")
            model_block.write(model_block_struct.read().replace("dertex", information3).replace("modid", information4))
            model_block.close()
            model_block_struct.close()

            model_item = open(f"models/item/{information1}.json", "w")
            model_item_struct = open("models/item/name.json", "r")
            model_item.write(model_item_struct.read().replace("name", information1).replace("modid", information4))
            model_item.close()
            model_item_struct.close()
            registry_code += registry_code + f'public static final RegistryObject<Block> {information1.upper()}_BLOCK = registerBlock("{information1}", () -> new Block(BlockBehaviour.Properties.copy(Blocks.{information5.upper()})));'

        registry_file.write(registry_code + "\n")

    registry_file.close()

    # Save the lang data
    with open(lang_file_path, "w") as lang_file:
        json.dump(lang_data, lang_file, indent=4)