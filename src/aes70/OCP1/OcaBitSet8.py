from .OcaUint8 import OcaUint8;

'''
 A set of 8 1-bit boolean flags. Used to signify (m) of (n)
 selections, where m &lt;= n. See AES70-Part 3 for rules for
 marshalling bit sets.
 @category Types
 @class OcaBitSet8
 @extends Base
'''

OcaBitSet8 = OcaUint8;
