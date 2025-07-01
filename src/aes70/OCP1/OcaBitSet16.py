from .OcaUint16 import OcaUint16;

'''
 A set of 16 1-bit boolean flags. Used to signify (m) of (n)
 selections, where m &lt;= n. See AES70-Part 3 for rules for
 marshalling bit sets.
 @category Types
 @class OcaBitSet16
 @extends Base
'''

OcaBitSet16 = OcaUint16;
