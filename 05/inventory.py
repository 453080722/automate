def displayInventory(inventory):
    '''
    展示目前的物品栏
    :param inventory: 玩家的物品栏
    :return: None
    '''
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print('{}  {}'.format(v, k))
        item_total += v
    print('Total number of items:{}'.format(item_total))


def addToInventory(inventory, addeditems):
    '''
    征服怪物后捡起掉落物更新物品栏
    :param inventory: 原来玩家的物品栏
    :param addeditems: 怪物的掉落物
    :return: 返回更新的物品栏
    '''
    for k in addeditems:
        if k in inventory:
            inventory[k] = inventory[k] + 1
        else:
            inventory.setdefault(k, 1)
    #print(inventory)
    return inventory

# 初始装备
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# 征服龙之后的掉落物
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
