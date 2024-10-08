#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, LVL_TO_ENG

mod = Mod('unlock_dlc3_tech.bl3hotfix',
        'Unlock DLC3 Tech',
        'Apocalyptech',
        [
            "Unlocks the various bits of 'Company' technology on Gehenna, in DLC3 (Bounty",
            "of Blood) right from the start, so you can use them all throughout the DLC.",
            "Does not unlock Breezebloom, since you get that so quickly.  Also this doesn't",
            "affect mission-related objects, such as the Coresploder you use to rescue",
            "Titus, or the Telezappers you're introduced to as part of the story missions.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='gameplay, qol',
        )

# The required objective that we'll reset things to
mission = '/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Mission_Ep01_ChildrenOfTheVault_C'
obj_name = 'Obj_GetAcrossBridgeGap_Objective'
obj_guid = '70fa4d4d4d4891f3482ec68258d0cce3'
objective = Mod.get_full_cond('/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Obj_GetAcrossBridgeGap_Objective', 'MissionObjective')
objref_stanza = f"""(
            Mission={mission},
            ObjectiveName="{obj_name}",
            ObjectiveGuid={obj_guid},
            Objective={objective}
        )"""

# It feels like I should be able to use "default" objects like this, to set it globally:
#
#   /Geranium/InteractiveObjects/Digiline/IO_Digiline.Default__IO_Digiline_C:Cond_DigilineAccessibllity_NewEnumerator0_MissionEnableConditionObjective
#
# However, I couldn't get that to work.  No matter, it's easy enough to do it individually.

# Generated by get_dlc3_tech.py, in dataprocessing dir
for attr_label, attr_name, data in [
        ('Traitorweed', 'Cond_GeraniumIOAccessibleState_NewEnumerator0_MissionEnableConditionObjective', [
            ('Forest_P', [
                '/Geranium/Maps/Forest/Forest_Art_B.Forest_Art_B:PersistentLevel.IO_GeraniumPlant_Taming_0',
                '/Geranium/Maps/Forest/Forest_Art_B.Forest_Art_B:PersistentLevel.IO_GeraniumPlant_Taming_10',
                '/Geranium/Maps/Forest/Forest_Art_C.Forest_Art_C:PersistentLevel.IO_GeraniumPlant_Taming_0',
                '/Geranium/Maps/Forest/Forest_Art_C.Forest_Art_C:PersistentLevel.IO_GeraniumPlant_Taming_1',
                '/Geranium/Maps/Forest/Forest_Art_C.Forest_Art_C:PersistentLevel.IO_GeraniumPlant_Taming_2',
                '/Geranium/Maps/Forest/Forest_Art_C.Forest_Art_C:PersistentLevel.IO_GeraniumPlant_Taming_4',
                '/Geranium/Maps/Forest/Forest_Art_C.Forest_Art_C:PersistentLevel.IO_GeraniumPlant_Taming_5',
                '/Geranium/Maps/Forest/Forest_Art_C.Forest_Art_C:PersistentLevel.IO_GeraniumPlant_Taming_9',
                '/Geranium/Maps/Forest/Forest_Art_D.Forest_Art_D:PersistentLevel.IO_GeraniumPlant_Taming_0',
                '/Geranium/Maps/Forest/Forest_Art_D.Forest_Art_D:PersistentLevel.IO_GeraniumPlant_Taming_27',
                '/Geranium/Maps/Forest/Forest_Art_E.Forest_Art_E:PersistentLevel.IO_GeraniumPlant_Taming_0',
                '/Geranium/Maps/Forest/Forest_Art_E.Forest_Art_E:PersistentLevel.IO_GeraniumPlant_Taming_1',
                '/Geranium/Maps/Forest/Forest_Art_E.Forest_Art_E:PersistentLevel.IO_GeraniumPlant_Taming_2',
                '/Geranium/Maps/Forest/Forest_Art_E.Forest_Art_E:PersistentLevel.IO_GeraniumPlant_Taming_7',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_0',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_1',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_15',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_16',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_2',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_27',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_3',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_5',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_6',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_7',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_8',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_GeraniumPlant_Taming_9',
                ]),
            ('Frontier_P', [
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Taming_2',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Taming_5',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Taming_8',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Taming_10',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Taming_2',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Taming_3',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Taming_5',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Taming_6',
                ]),
            ('Lodge_P', [
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_10',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_14',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_18',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_2',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_22',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_26',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_3',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_30',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_34',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Taming_6',
                '/Geranium/Maps/Lodge/Lodge_Dynamic.Lodge_Dynamic:PersistentLevel.IO_GeraniumPlant_Taming_2',
                ]),
            ('Town_P', [
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Taming_11',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Taming_2',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Taming_8',
                ]),
            ]),
        ('Telezappers', 'Cond_DigilineAccessibllity_NewEnumerator0_MissionEnableConditionObjective', [
            ('Forest_P', [
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_Digiline_1A',
                '/Geranium/Maps/Forest/Forest_Combat.Forest_Combat:PersistentLevel.IO_Digiline_1B',
                ]),
            ('Frontier_P', [
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_Digiline_4A',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_Digiline_4B',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_Digiline_5A',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_Digiline_5B',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_Digiline_6A',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_Digiline_6B',
                '/Geranium/Maps/Frontier/Frontier_P.Frontier_P:PersistentLevel.IO_Digiline_3A',
                '/Geranium/Maps/Frontier/Frontier_P.Frontier_P:PersistentLevel.IO_Digiline_3B',
                ]),
            ('Lodge_P', [
                '/Geranium/Maps/Lodge/Lodge_Dynamic.Lodge_Dynamic:PersistentLevel.IO_Digiline_2A',
                '/Geranium/Maps/Lodge/Lodge_Dynamic.Lodge_Dynamic:PersistentLevel.IO_Digiline_2B',
                '/Geranium/Maps/Lodge/Lodge_Interior_Geo.Lodge_Interior_Geo:PersistentLevel.IO_Digiline_1A',
                '/Geranium/Maps/Lodge/Lodge_Interior_Geo.Lodge_Interior_Geo:PersistentLevel.IO_Digiline_1B',
                ]),
            ('Town_P', [
                '/Geranium/Maps/Town/Town_Bunker.Town_Bunker:PersistentLevel.IO_Digiline_1A',
                '/Geranium/Maps/Town/Town_Bunker.Town_Bunker:PersistentLevel.IO_Digiline_1B',
                '/Geranium/Maps/Town/Town_Dynamic.Town_Dynamic:PersistentLevel.IO_Digiline_2A',
                '/Geranium/Maps/Town/Town_Dynamic.Town_Dynamic:PersistentLevel.IO_Digiline_2B',
                '/Geranium/Maps/Town/Town_Dynamic.Town_Dynamic:PersistentLevel.IO_Digiline_3A',
                '/Geranium/Maps/Town/Town_Dynamic.Town_Dynamic:PersistentLevel.IO_Digiline_3B',
                ]),
            ]),
        ('Coresploders', 'Cond_GeraniumIOAccessibleState_NewEnumerator0_MissionEnableConditionObjective', [
            ('Frontier_P', [
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_12',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_16',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_2',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_20',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_24',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_28',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_3',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_31',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_35',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_38',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_4',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_42',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_45',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_48',
                '/Geranium/Maps/Frontier/Frontier_Combat.Frontier_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_5',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_10',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_11',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_13',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_14',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_15',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_16',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_17',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_18',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_19',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_2',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_22',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_23',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_24',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_26',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_27',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_3',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_30',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_31',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_32',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_36',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_4',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_40',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_44',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_48',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_5',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_52',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_56',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_6',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_60',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_7',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_8',
                '/Geranium/Maps/Frontier/Frontier_Dynamic.Frontier_Dynamic:PersistentLevel.IO_GeraniumPlant_Rocksploder_9',
                '/Geranium/Maps/Frontier/Frontier_P.Frontier_P:PersistentLevel.IO_GeraniumPlant_Rocksploder_1',
                ]),
            ('Lodge_P', [
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_RocksploderWall_2',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_RocksploderWall_5',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_10',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_11',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_14',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_15',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_2',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_26',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_27',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_30',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_4',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_5',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_6',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_7',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_8',
                '/Geranium/Maps/Lodge/Lodge_Combat.Lodge_Combat:PersistentLevel.IO_GeraniumPlant_Rocksploder_9',
                '/Geranium/Maps/Lodge/Lodge_Interior_Geo.Lodge_Interior_Geo:PersistentLevel.IO_GeraniumPlant_RocksploderWall_2',
                '/Geranium/Maps/Lodge/Lodge_LeadUpToLodge_Geo.Lodge_LeadUpToLodge_Geo:PersistentLevel.IO_GeraniumPlant_RocksploderWall_2',
                '/Geranium/Maps/Lodge/Lodge_LeadUpToLodge_Geo.Lodge_LeadUpToLodge_Geo:PersistentLevel.IO_GeraniumPlant_RocksploderWall_6',
                '/Geranium/Maps/Lodge/Lodge_MountainPass_Geo.Lodge_MountainPass_Geo:PersistentLevel.IO_GeraniumPlant_RocksploderWall_0',
                '/Geranium/Maps/Lodge/Lodge_TheLegendOfMcSmugger_Geo.Lodge_TheLegendOfMcSmugger_Geo:PersistentLevel.IO_GeraniumPlant_Rocksploder_2',
                '/Geranium/Maps/Lodge/Lodge_TheLegendOfMcSmugger_Geo.Lodge_TheLegendOfMcSmugger_Geo:PersistentLevel.IO_GeraniumPlant_Rocksploder_3',
                ]),
            ('Town_P', [
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_10',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_13',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_17',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_2',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_21',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_28',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_31',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_35',
                '/Geranium/Maps/Town/Town_Interior.Town_Interior:PersistentLevel.IO_GeraniumPlant_Rocksploder_6',
                ]),
            ]),
        ]:

    mod.header(attr_label)

    for level_name, io_names in data:

        mod.comment(LVL_TO_ENG[level_name])

        for io_name in io_names:

            mod.reg_hotfix(Mod.LEVEL, level_name,
                    f'{io_name}.{attr_name}',
                    'ObjectiveRef',
                    objref_stanza)

        mod.newline()

mod.close()

