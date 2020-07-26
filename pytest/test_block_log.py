from pyeoskit import block_log
p = block_log.BlockParser('data-dir')
p.repair_block(10)
