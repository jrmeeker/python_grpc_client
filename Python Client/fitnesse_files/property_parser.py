
def parse_property(prop):
    levels = prop.split('.')
    print(levels)

if __name__ == '__main__':
    parse_property('SubBlock[0].CompCarriers[0].DownlinkTestModelDuplexScheme')
