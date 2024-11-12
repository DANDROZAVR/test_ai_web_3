import { IERC2981 } from "openzeppelin-contracts/interfaces/IERC2981.sol";

import {
    AllowListData,
    PublicDrop,
    TokenGatedDropStage,
    SignedMintValidationParams
import { ERC721ACloneable } from "./ERC721ACloneable.sol";

     contract ERC721SeaDropCloneable is
    ERC721ContractMetadataCloneable,
    INonFungibleSeaDropToken,
    ERC721SeaDropStructsErrorsAndEvents,
    ReentrancyGuardUpgradeable
  import { ERC721ACloneable } from "./ERC721ACloneable.sol";

 pragma solidity 0.8.17;

