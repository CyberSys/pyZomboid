
import re
import logging
from zomboid.java import ArrayList
from .base import BaseScriptObject 
logger = logging.getLogger(__name__)

class Item(BaseScriptObject):
    BodyLocation : str = ""
    Palettes : ArrayList = None
    HitSound : str = "BatHit"
    HitFloorSound : str = "BatOnFloor"
    PalettesStart : str = ""
    DisplayName : str = None
    MetalValue : float = 0.0
    SpriteName : str = None
    SplatSize : float = 1.0
    Type : str = "Normal"
    CanStoreWater : bool = False
    IsWaterSource : bool = False
    Poison : bool = False
    FoodType : str = None
    PoisonDetectionLevel : int = None
    PoisonPower : int = 0
    UseForPoison : int = None
    SwingAnim : str = "Rifle"
    Icon : str = "None"
    UseWorldItem : bool = False
    Medical : bool = False
    CannedFood : bool = False
    MechanicsItem : bool = False
    SurvivalGear : bool = False
    ScaleWorldIcon : float = 1.0
    HairDye : bool = False
    DoorHitSound : str = "ChopDoor"
    ActualWeight : float = 1.0
    WeightWet : float = 0.0
    WeightEmpty : float = 0.0
    HungerChange : float = 0.0
    ThirstChange : float = 0.0
    FatigueChange : float = 0.0
    EnduranceChange : float = 0.0
    CriticalChance : float = None
    critDmgMultiplier : float = None
    DaysFresh : int = None
    DaysTotallyRotten : int = None
    IsCookable : bool = False
    MinutesToCook : int = 60
    MinutesToBurn : int = 120
    BoredomChange : int = 0
    StressChange : int = 0
    UnhappyChange : int = 0
    ReplaceOnDeplete : str = None
    ReplaceOnUseOn : str = None
    Ranged : bool = False
    UseSelf : bool = False
    OtherHandUse : bool = False
    DangerousUncooked : bool = False
    MaxRange : float = 1.0
    MinRange : float = 0.0
    MinAngle : float = 1.0
    MaxDamage : float = 1.5
    baseSpeed : float = 1.0
    stompPower : float = 1.0
    combatSpeedModifier : float = 1.0
    runSpeedModifier : float = 1.0
    clothingItemExtra : ArrayList = None
    clothingExtraSubmenu : str = None
    removeOnBroken : bool = False
    canHaveHoles : bool = True
    cosmetic : bool = False
    ammoBox : str = None
    insertAmmoSound : str = None
    ejectAmmoSound : str = None
    rackSound : str = None
    clickSound : str = "Stormy9mmClick"
    magazineType : str = None
    jamGunChance : float = 1.0
    modelWeaponPart : ArrayList = 1.0
    rackAfterShoot : bool = False
    haveChamber : bool = True
    biteDefense : float = 0.0
    neckProtectionModifier : float = 1.0
    damageCategory : str = None
    fireMode : str = None
    damageMakeHole : bool = False
    equippedNoSprint : bool = False
    scratchDefense : float = 0.0
    weaponReloadType : str = None
    insertAllBulletsReload : bool = False
    clothingItemExtraOption : ArrayList = None
    ConditionLowerChanceOneIn : int = 1000000
    MultipleHitConditionAffected : bool = True
    CanBandage : bool = False
    ConditionMax : int = 10
    SoundGain : float = 1.0
    MinDamage : float = 0.0
    MinimumSwingTime : float = 0.0
    SwingSound : str = "BatSwing"
    ReplaceOnUse : str = None
    WeaponSprite : str = None
    AimingPerkCritModifier : int = 0
    AimingPerkRangeModifier : float = 0.0
    AimingPerkHitChanceModifier : float = 0.0
    angleModifier : float = 0.0
    weightModifier : float = 0.0
    AimingPerkMinAngleModifier : float = 0.0
    HitChance : int = 0
    RecoilDelay : int = 0
    PiercingBullets : bool = False
    AngleFalloff : bool = False
    SoundVolume : int = 0
    ToHitModifier : float = 1.0
    SoundRadius : int = 0
    Categories : ArrayList = None
    OtherCharacterVolumeBoost : float = None
    ImpactSound : str = "ZombieImpact"
    SwingTime : float = 1.0
    KnockBackOnNoDeath : bool = True
    Alcoholic : bool = False
    SplatBloodOnNoDeath : bool = False
    SwingAmountBeforeImpact : float = 0.0
    AmmoType : str = None
    maxAmmo : int = 0
    HitAngleMod : float = 0.0
    OtherHandRequire : str = None
    AlwaysWelcomeGift : bool = False
    CantAttackWithLowestEndurance : bool = False
    EnduranceMod : float = 1.0
    KnockdownMod : float = 1.0
    DoorDamage : int = 1
    MaxHitCount : int = 1000
    PhysicsObject : str = None
    Count : int = 1
    WeaponWeight : float = 1.0
    IdleAnim : str = "Idle"
    RunAnim : str = "Run"
    RequireInHandOrInventory : ArrayList = None
    fireModePossibilities : ArrayList = None
    attachmentsProvided : ArrayList = None
    attachmentReplacement : str = None
    PushBackMod : float = 1.0
    NPCSoundBoost : float = 1.0
    SplatNumber : int = 2
    RangeFalloff : bool = False
    UseEndurance : bool = True
    ShareDamage : bool = True
    ShareEndurance : bool = False
    AlwaysKnockdown : bool = False
    IsAimedFirearm : bool = False
    bulletOutSound : str = None
    ShellFallSound : str = None
    IsAimedHandWeapon : bool = False
    AimingMod : float = 1.0
    ProjectileCount : int = 1
    CanStack : bool = True
    HerbalistType : str = None
    CanBarricade : bool = False
    UseWhileEquipped : bool = True
    TicksPerEquipUse : int = 30
    DisappearOnUse : bool = True
    Temperature : float = 0.0
    insulation : float = 0.0
    windresist : float = 0.0
    waterresist : float = 0.0
    CloseKillMove : str = None
    UseDelta : float = 0.03125
    rainFactor : float = None
    torchDot : float = 0.96
    NumberOfPages : int = -1
    SkillTrained : str = ""
    LvlSkillTrained : int = -1
    NumLevelsTrained : int = 1
    Capacity : int = 0
    maxCapacity : int = -1
    itemCapacity : int = -1
    ConditionAffectsCapacity : bool = False
    brakeForce : int = 0
    chanceToSpawnDamaged : int = 0
    WeaponLength : float = 0.4
    ClipSize : int = 0
    reloadTime : int = 0
    aimingTime : int = 0
    aimingTimeModifier : int = 0
    reloadTimeModifier : int = 0
    hitChanceModifier : int = 0
    WeightReduction : int = 0
    CanBeEquipped : str = ""
    SubCategory : str = ""
    ActivatedItem : bool = False
    ProtectFromRainWhenEquipped : bool = False
    LightStrength : float = 0.0
    TorchCone : bool = False
    LightDistance : int = 0
    TwoHandWeapon : bool = False
    Tooltip : str = None
    DisplayCategory : str = None
    BadInMicrowave : bool = False
    GoodHot : bool = False
    BadCold : bool = False
    AlarmSound : str = None
    RequiresEquippedBothHands : bool = False
    ReplaceOnCooked : ArrayList = None
    CustomContextMenu : str = None
    Trap : bool = False
    isWet : bool = False
    wetCooldown : float = 0.0
    itemWhenDry : str = None
    FishingLure : bool = False
    canBeWrite : bool = False
    PageToWrite : int = 0
    Spice : bool = False
    RemoveNegativeEffectOnCooked : bool = False
    clipSizeModifier : int = 0
    recoilDelayModifier : float = 0.0
    maxRangeModifier : float = 0.0
    minRangeRangedModifier : float = 0.0
    damageModifier : float = 0.0
    map : str = None
    PutInSound : str = None
    CloseSound : str = None
    OpenSound : str = None
    breakSound : str = None
    treeDamage : int = 0
    customEatSound : str = None
    alcoholPower : float = 0.0
    bandagePower : float = 0.0
    ReduceInfectionPower : float = 0.0
    OnCooked : str = None
    OnlyAcceptCategory : str = None
    padlock : bool = False
    digitalPadlock : bool = False
    triggerExplosionTimer : int = 0
    sensorRange : int = 0
    remoteRange : int = 0
    countDownSound : str = None
    explosionSound : str = None
    PlacedSprite : str = None
    explosionTimer : int = 0
    explosionRange : int = 0
    explosionPower : int = 0
    fireRange : int = 0
    firePower : int = 0
    canBePlaced : bool = False
    canBeReused : bool = False
    canBeRemote : bool = False
    remoteController : bool = False
    smokeRange : int = 0
    noiseRange : int = 0
    extraDamage : float = 0.0
    twoWay : bool = False
    transmitRange : int = 0
    micRange : int = 0
    baseVolumeRange : float = 0.0
    isPortable : bool = False
    isTelevision : bool = False
    minChannel : int = 88000
    maxChannel : int = 108000
    usesBattery : bool = False
    isHighTier : bool = False
    worldObjectSprite : str = None
    fluReduction : int = 0
    ReduceFoodSickness : int = 0
    painReduction : int = 0
    colorRed : int = 255
    colorGreen : int = 255
    colorBlue : int = 255
    calories : float = 0.0
    carbohydrates : float = 0.0
    lipids : float = 0.0
    proteins : float = 0.0
    packaged : bool = False
    cantBeFrozen : bool = False
    evolvedRecipeName : str = None
    ReplaceOnRotten : str = None
    cantBeConsolided : bool = False
    onEat : str = None
    keepOnDeplete : bool = False
    vehicleType : int = 0
    chanceToFall : int = 0
    conditionLowerOffroad : float = 0.0
    conditionLowerNormal : float = 0.0
    wheelFriction : float = 0.0
    suspensionDamping : float = 0.0
    suspensionCompression : float = 0.0
    engineLoudness : float = 0.0
    attachmentType : str = None
    makeUpType : str = None
    consolidateOption : str = None
    fabricType : str = None
    teachedRecipes : ArrayList = None
    mountOn : ArrayList = None
    partType : str = None
    ClothingItem : str = None
    staticModel : str = None
    primaryAnimMask : str = None
    secondaryAnimMask : str = None
    primaryAnimMaskAttachment : str = None
    secondaryAnimMaskAttachment : str = None
    replaceInSecondHand : str = None
    replaceInPrimaryHand : str = None
    replaceWhenUnequip : str = None
    eatType : str = None
    IconsForTexture : ArrayList = None
    bloodClothingType : ArrayList = None
    OBSOLETE : bool = False

    def Load(self, name : str, data : list) -> None:
        self.name = name
        for line in data:
            self.DoParam(line)

    def DoParam(self, line : str) -> None:
        line = line.strip()
        if not line:
            return

        match = re.match(r"^\s*(\S+)\s*:\s*(.+?)\s*$", line)
        if not match:
            return

        key, value = match.groups()
        key = key.lower()
        if key == 'bodylocation':
            self.BodyLocation = value

        elif key == 'palettes':
            self.Palettes = ArrayList(value.split('/'))

        elif key == 'hitsound':
            self.HitSound = value

        elif key == 'hitfloorsound':
            self.HitFloorSound = value

        elif key == 'palettesstart':
            self.PalettesStart = value

        elif key == 'displayname':
            self.DisplayName = value

        elif key == 'metalvalue':
            self.MetalValue = float(value)

        elif key == 'spritename':
            self.SpriteName = value

        elif key == 'splatsize':
            self.SplatSize = float(value)

        elif key == 'type':
            self.Type = value

        elif key == 'canstorewater':
            self.CanStoreWater = value.lower() == 'true'

        elif key == 'iswatersource':
            self.IsWaterSource = value.lower() == 'true'

        elif key == 'poison':
            self.Poison = value.lower() == 'true'

        elif key == 'foodtype':
            self.FoodType = value

        elif key == 'poisondetectionlevel':
            self.PoisonDetectionLevel = int(value)

        elif key == 'poisonpower':
            self.PoisonPower = int(value)

        elif key == 'useforpoison':
            self.UseForPoison = int(value)

        elif key == 'swinganim':
            self.SwingAnim = value

        elif key == 'icon':
            self.Icon = value

        elif key == 'useworlditem':
            self.UseWorldItem = value.lower() == 'true'

        elif key == 'medical':
            self.Medical = value.lower() == 'true'

        elif key == 'cannedfood':
            self.CannedFood = value.lower() == 'true'

        elif key == 'mechanicsitem':
            self.MechanicsItem = value.lower() == 'true'

        elif key == 'survivalgear':
            self.SurvivalGear = value.lower() == 'true'

        elif key == 'scaleworldicon':
            self.ScaleWorldIcon = float(value)

        elif key == 'hairdye':
            self.HairDye = value.lower() == 'true'

        elif key == 'doorhitsound':
            self.DoorHitSound = value

        elif key == 'weight':
            self.ActualWeight = float(value)

        elif key == 'weightwet':
            self.WeightWet = float(value)

        elif key == 'weightempty':
            self.WeightEmpty = float(value)

        elif key == 'hungerchange':
            self.HungerChange = float(value)

        elif key == 'thirstchange':
            self.ThirstChange = float(value)

        elif key == 'fatiguechange':
            self.FatigueChange = float(value)

        elif key == 'endurancechange':
            self.EnduranceChange = float(value)

        elif key == 'criticalchance':
            self.CriticalChance = float(value)

        elif key == 'critdmgmultiplier':
            self.critDmgMultiplier = float(value)

        elif key == 'daysfresh':
            self.DaysFresh = int(value)

        elif key == 'daystotallyrotten':
            self.DaysTotallyRotten = int(value)

        elif key == 'iscookable':
            self.IsCookable = value.lower() == 'true'

        elif key == 'minutestocook':
            self.MinutesToCook = int(value)

        elif key == 'minutestoburn':
            self.MinutesToBurn = int(value)

        elif key == 'boredomchange':
            self.BoredomChange = int(value)

        elif key == 'stresschange':
            self.StressChange = int(value)

        elif key == 'unhappychange':
            self.UnhappyChange = int(value)

        elif key == 'replaceondeplete':
            self.ReplaceOnDeplete = value

        elif key == 'replaceonuseon':
            self.ReplaceOnUseOn = value

        elif key == 'ranged':
            self.Ranged = value.lower() == 'true'

        elif key == 'useself':
            self.UseSelf = value.lower() == 'true'

        elif key == 'otherhanduse':
            self.OtherHandUse = value.lower() == 'true'

        elif key == 'dangerousuncooked':
            self.DangerousUncooked = value.lower() == 'true'

        elif key == 'maxrange':
            self.MaxRange = float(value)

        elif key == 'minrange':
            self.MinRange = float(value)

        elif key == 'minangle':
            self.MinAngle = float(value)

        elif key == 'maxdamage':
            self.MaxDamage = float(value)

        elif key == 'basespeed':
            self.baseSpeed = float(value)

        elif key == 'stomppower':
            self.stompPower = float(value)

        elif key == 'combatspeedmodifier':
            self.combatSpeedModifier = float(value)

        elif key == 'runspeedmodifier':
            self.runSpeedModifier = float(value)

        elif key == 'clothingitemextra':
            self.clothingItemExtra = ArrayList(value.split(';'))

        elif key == 'clothingextrasubmenu':
            self.clothingExtraSubmenu = value

        elif key == 'removeonbroken':
            self.removeOnBroken = value.lower() == 'true'

        elif key == 'canhaveholes':
            self.canHaveHoles = value.lower() == 'true'

        elif key == 'cosmetic':
            self.cosmetic = value.lower() == 'true'

        elif key == 'ammobox':
            self.ammoBox = value

        elif key == 'insertammosound':
            self.insertAmmoSound = value

        elif key == 'ejectammosound':
            self.ejectAmmoSound = value

        elif key == 'racksound':
            self.rackSound = value

        elif key == 'clicksound':
            self.clickSound = value

        elif key == 'magazinetype':
            self.magazineType = value

        elif key == 'jamgunchance':
            self.jamGunChance = float(value)

        elif key == 'modelweaponpart':
            self.modelWeaponPart = ArrayList(value.split(' '))

        elif key == 'rackaftershoot':
            self.rackAfterShoot = value.lower() == 'true'

        elif key == 'havechamber':
            self.haveChamber = value.lower() == 'true'

        elif key == 'bitedefense':
            self.biteDefense = float(value)

        elif key == 'neckprotectionmodifier':
            self.neckProtectionModifier = float(value)

        elif key == 'damagecategory':
            self.damageCategory = value

        elif key == 'firemode':
            self.fireMode = value

        elif key == 'damagemakehole':
            self.damageMakeHole = value.lower() == 'true'

        elif key == 'equippednosprint':
            self.equippedNoSprint = value.lower() == 'true'

        elif key == 'scratchdefense':
            self.scratchDefense = float(value)

        elif key == 'weaponreloadtype':
            self.weaponReloadType = value

        elif key == 'insertallbulletsreload':
            self.insertAllBulletsReload = value.lower() == 'true'

        elif key == 'clothingitemextraoption':
            self.clothingItemExtraOption = ArrayList(value.split(';'))

        elif key == 'conditionlowerchance':
            self.ConditionLowerChanceOneIn = int(value)

        elif key == 'multiplehitconditionaffected':
            self.MultipleHitConditionAffected = value.lower() == 'true'

        elif key == 'canbandage':
            self.CanBandage = value.lower() == 'true'

        elif key == 'conditionmax':
            self.ConditionMax = int(value)

        elif key == 'soundgain':
            self.SoundGain = float(value)

        elif key == 'mindamage':
            self.MinDamage = float(value)

        elif key == 'minimumswingtime':
            self.MinimumSwingTime = float(value)

        elif key == 'swingsound':
            self.SwingSound = value

        elif key == 'replaceonuse':
            self.ReplaceOnUse = value

        elif key == 'weaponsprite':
            self.WeaponSprite = value

        elif key == 'aimingperkcritmodifier':
            self.AimingPerkCritModifier = int(value)

        elif key == 'aimingperkrangemodifier':
            self.AimingPerkRangeModifier = float(value)

        elif key == 'aimingperkhitchancemodifier':
            self.AimingPerkHitChanceModifier = float(value)

        elif key == 'anglemodifier':
            self.angleModifier = float(value)

        elif key == 'weightmodifier':
            self.weightModifier = float(value)

        elif key == 'aimingperkminanglemodifier':
            self.AimingPerkMinAngleModifier = float(value)

        elif key == 'hitchance':
            self.HitChance = int(value)

        elif key == 'recoildelay':
            self.RecoilDelay = int(value)

        elif key == 'piercingbullets':
            self.PiercingBullets = value.lower() == 'true'

        elif key == 'anglefalloff':
            self.AngleFalloff = value.lower() == 'true'

        elif key == 'soundvolume':
            self.SoundVolume = int(value)

        elif key == 'tohitmodifier':
            self.ToHitModifier = float(value)

        elif key == 'soundradius':
            self.SoundRadius = int(value)

        elif key == 'categories':
            self.Categories = ArrayList(value.split(';'))

        elif key == 'othercharactervolumeboost':
            self.OtherCharacterVolumeBoost = float(value)

        elif key == 'impactsound':
            self.ImpactSound = value

        elif key == 'swingtime':
            self.SwingTime = float(value)

        elif key == 'knockbackonnodeath':
            self.KnockBackOnNoDeath = value.lower() == 'true'

        elif key == 'alcoholic':
            self.Alcoholic = value.lower() == 'true'

        elif key == 'splatbloodonnodeath':
            self.SplatBloodOnNoDeath = value.lower() == 'true'

        elif key == 'swingamountbeforeimpact':
            self.SwingAmountBeforeImpact = float(value)

        elif key == 'ammotype':
            self.AmmoType = value

        elif key == 'maxammo':
            self.maxAmmo = int(value)

        elif key == 'hitanglemod':
            self.HitAngleMod = float(value)

        elif key == 'otherhandrequire':
            self.OtherHandRequire = value

        elif key == 'alwayswelcomegift':
            self.AlwaysWelcomeGift = value.lower() == 'true'

        elif key == 'cantattackwithlowestendurance':
            self.CantAttackWithLowestEndurance = value.lower() == 'true'

        elif key == 'endurancemod':
            self.EnduranceMod = float(value)

        elif key == 'knockdownmod':
            self.KnockdownMod = float(value)

        elif key == 'doordamage':
            self.DoorDamage = int(value)

        elif key == 'maxhitcount':
            self.MaxHitCount = int(value)

        elif key == 'physicsobject':
            self.PhysicsObject = value

        elif key == 'count':
            self.Count = int(value)

        elif key == 'weaponweight':
            self.WeaponWeight = float(value)

        elif key == 'idleanim':
            self.IdleAnim = value

        elif key == 'runanim':
            self.RunAnim = value

        elif key == 'requireinhandorinventory':
            self.RequireInHandOrInventory = ArrayList(value.split('/'))

        elif key == 'firemodepossibilities':
            self.fireModePossibilities = ArrayList(value.split('/'))

        elif key == 'attachmentsprovided':
            self.attachmentsProvided = ArrayList(value.split(';'))

        elif key == 'attachmentreplacement':
            self.attachmentReplacement = value

        elif key == 'pushbackmod':
            self.PushBackMod = float(value)

        elif key == 'npcsoundboost':
            self.NPCSoundBoost = float(value)

        elif key == 'splatnumber':
            self.SplatNumber = int(value)

        elif key == 'rangefalloff':
            self.RangeFalloff = value.lower() == 'true'

        elif key == 'useendurance':
            self.UseEndurance = value.lower() == 'true'

        elif key == 'sharedamage':
            self.ShareDamage = value.lower() == 'true'

        elif key == 'shareendurance':
            self.ShareEndurance = value.lower() == 'true'

        elif key == 'alwaysknockdown':
            self.AlwaysKnockdown = value.lower() == 'true'

        elif key == 'isaimedfirearm':
            self.IsAimedFirearm = value.lower() == 'true'

        elif key == 'bulletoutsound':
            self.bulletOutSound = value

        elif key == 'shellfallsound':
            self.ShellFallSound = value

        elif key == 'isaimedhandweapon':
            self.IsAimedHandWeapon = value.lower() == 'true'

        elif key == 'aimingmod':
            self.AimingMod = float(value)

        elif key == 'projectilecount':
            self.ProjectileCount = int(value)

        elif key == 'canstack':
            self.CanStack = value.lower() == 'true'

        elif key == 'herbalisttype':
            self.HerbalistType = value

        elif key == 'canbarricade':
            self.CanBarricade = value.lower() == 'true'

        elif key == 'usewhileequipped':
            self.UseWhileEquipped = value.lower() == 'true'

        elif key == 'ticksperequipuse':
            self.TicksPerEquipUse = int(value)

        elif key == 'disappearonuse':
            self.DisappearOnUse = value.lower() == 'true'

        elif key == 'temperature':
            self.Temperature = float(value)

        elif key == 'insulation':
            self.insulation = float(value)

        elif key == 'windresistance':
            self.windresist = float(value)

        elif key == 'waterresistance':
            self.waterresist = float(value)

        elif key == 'closekillmove':
            self.CloseKillMove = value

        elif key == 'usedelta':
            self.UseDelta = float(value)

        elif key == 'rainfactor':
            self.rainFactor = float(value)

        elif key == 'torchdot':
            self.torchDot = float(value)

        elif key == 'numberofpages':
            self.NumberOfPages = int(value)

        elif key == 'skilltrained':
            self.SkillTrained = value

        elif key == 'lvlskilltrained':
            self.LvlSkillTrained = int(value)

        elif key == 'numlevelstrained':
            self.NumLevelsTrained = int(value)

        elif key == 'capacity':
            self.Capacity = int(value)

        elif key == 'maxcapacity':
            self.maxCapacity = int(value)

        elif key == 'itemcapacity':
            self.itemCapacity = int(value)

        elif key == 'conditionaffectscapacity':
            self.ConditionAffectsCapacity = value.lower() == 'true'

        elif key == 'brakeforce':
            self.brakeForce = int(value)

        elif key == 'chancetospawndamaged':
            self.chanceToSpawnDamaged = int(value)

        elif key == 'weaponlength':
            self.WeaponLength = float(value)

        elif key == 'clipsize':
            self.ClipSize = int(value)

        elif key == 'reloadtime':
            self.reloadTime = int(value)

        elif key == 'aimingtime':
            self.aimingTime = int(value)

        elif key == 'aimingtimemodifier':
            self.aimingTimeModifier = int(value)

        elif key == 'reloadtimemodifier':
            self.reloadTimeModifier = int(value)

        elif key == 'hitchancemodifier':
            self.hitChanceModifier = int(value)

        elif key == 'weightreduction':
            self.WeightReduction = int(value)

        elif key == 'canbeequipped':
            self.CanBeEquipped = value

        elif key == 'subcategory':
            self.SubCategory = value

        elif key == 'activateditem':
            self.ActivatedItem = value.lower() == 'true'

        elif key == 'protectfromrainwhenequipped':
            self.ProtectFromRainWhenEquipped = value.lower() == 'true'

        elif key == 'lightstrength':
            self.LightStrength = float(value)

        elif key == 'torchcone':
            self.TorchCone = value.lower() == 'true'

        elif key == 'lightdistance':
            self.LightDistance = int(value)

        elif key == 'twohandweapon':
            self.TwoHandWeapon = value.lower() == 'true'

        elif key == 'tooltip':
            self.Tooltip = value

        elif key == 'displaycategory':
            self.DisplayCategory = value

        elif key == 'badinmicrowave':
            self.BadInMicrowave = value.lower() == 'true'

        elif key == 'goodhot':
            self.GoodHot = value.lower() == 'true'

        elif key == 'badcold':
            self.BadCold = value.lower() == 'true'

        elif key == 'alarmsound':
            self.AlarmSound = value

        elif key == 'requiresequippedbothhands':
            self.RequiresEquippedBothHands = value.lower() == 'true'

        elif key == 'replaceoncooked':
            self.ReplaceOnCooked = ArrayList(value.split(';'))

        elif key == 'customcontextmenu':
            self.CustomContextMenu = value

        elif key == 'trap':
            self.Trap = value.lower() == 'true'

        elif key == 'wet':
            self.isWet = value.lower() == 'true'

        elif key == 'wetcooldown':
            self.wetCooldown = float(value)

        elif key == 'itemwhendry':
            self.itemWhenDry = value

        elif key == 'fishinglure':
            self.FishingLure = value.lower() == 'true'

        elif key == 'canbewrite':
            self.canBeWrite = value.lower() == 'true'

        elif key == 'pagetowrite':
            self.PageToWrite = int(value)

        elif key == 'spice':
            self.Spice = value.lower() == 'true'

        elif key == 'removenegativeeffectoncooked':
            self.RemoveNegativeEffectOnCooked = value.lower() == 'true'

        elif key == 'clipsizemodifier':
            self.clipSizeModifier = int(value)

        elif key == 'recoildelaymodifier':
            self.recoilDelayModifier = float(value)

        elif key == 'maxrangemodifier':
            self.maxRangeModifier = float(value)

        elif key == 'minrangerangedmodifier':
            self.minRangeRangedModifier = float(value)

        elif key == 'damagemodifier':
            self.damageModifier = float(value)

        elif key == 'map':
            self.map = value

        elif key == 'putinsound':
            self.PutInSound = value

        elif key == 'closesound':
            self.CloseSound = value

        elif key == 'opensound':
            self.OpenSound = value

        elif key == 'breaksound':
            self.breakSound = value

        elif key == 'treedamage':
            self.treeDamage = int(value)

        elif key == 'customeatsound':
            self.customEatSound = value

        elif key == 'alcoholpower':
            self.alcoholPower = float(value)

        elif key == 'bandagepower':
            self.bandagePower = float(value)

        elif key == 'reduceinfectionpower':
            self.ReduceInfectionPower = float(value)

        elif key == 'oncooked':
            self.OnCooked = value

        elif key == 'onlyacceptcategory':
            self.OnlyAcceptCategory = value

        elif key == 'padlock':
            self.padlock = value.lower() == 'true'

        elif key == 'digitalpadlock':
            self.digitalPadlock = value.lower() == 'true'

        elif key == 'triggerexplosiontimer':
            self.triggerExplosionTimer = int(value)

        elif key == 'sensorrange':
            self.sensorRange = int(value)

        elif key == 'remoterange':
            self.remoteRange = int(value)

        elif key == 'countdownsound':
            self.countDownSound = value

        elif key == 'explosionsound':
            self.explosionSound = value

        elif key == 'placedsprite':
            self.PlacedSprite = value

        elif key == 'explosiontimer':
            self.explosionTimer = int(value)

        elif key == 'explosionrange':
            self.explosionRange = int(value)

        elif key == 'explosionpower':
            self.explosionPower = int(value)

        elif key == 'firerange':
            self.fireRange = int(value)

        elif key == 'firepower':
            self.firePower = int(value)

        elif key == 'canbeplaced':
            self.canBePlaced = value.lower() == 'true'

        elif key == 'canbereused':
            self.canBeReused = value.lower() == 'true'

        elif key == 'canberemote':
            self.canBeRemote = value.lower() == 'true'

        elif key == 'remotecontroller':
            self.remoteController = value.lower() == 'true'

        elif key == 'smokerange':
            self.smokeRange = int(value)

        elif key == 'noiserange':
            self.noiseRange = int(value)

        elif key == 'extradamage':
            self.extraDamage = float(value)

        elif key == 'twoway':
            self.twoWay = value.lower() == 'true'

        elif key == 'transmitrange':
            self.transmitRange = int(value)

        elif key == 'micrange':
            self.micRange = int(value)

        elif key == 'basevolumerange':
            self.baseVolumeRange = float(value)

        elif key == 'isportable':
            self.isPortable = value.lower() == 'true'

        elif key == 'istelevision':
            self.isTelevision = value.lower() == 'true'

        elif key == 'minchannel':
            self.minChannel = int(value)

        elif key == 'maxchannel':
            self.maxChannel = int(value)

        elif key == 'usesbattery':
            self.usesBattery = value.lower() == 'true'

        elif key == 'ishightier':
            self.isHighTier = value.lower() == 'true'

        elif key == 'worldobjectsprite':
            self.worldObjectSprite = value

        elif key == 'flureduction':
            self.fluReduction = int(value)

        elif key == 'reducefoodsickness':
            self.ReduceFoodSickness = int(value)

        elif key == 'painreduction':
            self.painReduction = int(value)

        elif key == 'colorred':
            self.colorRed = int(value)

        elif key == 'colorgreen':
            self.colorGreen = int(value)

        elif key == 'colorblue':
            self.colorBlue = int(value)

        elif key == 'calories':
            self.calories = float(value)

        elif key == 'carbohydrates':
            self.carbohydrates = float(value)

        elif key == 'lipids':
            self.lipids = float(value)

        elif key == 'proteins':
            self.proteins = float(value)

        elif key == 'packaged':
            self.packaged = value.lower() == 'true'

        elif key == 'cantbefrozen':
            self.cantBeFrozen = value.lower() == 'true'

        elif key == 'evolvedrecipename':
            self.evolvedRecipeName = value

        elif key == 'replaceonrotten':
            self.ReplaceOnRotten = value

        elif key == 'cantbeconsolided':
            self.cantBeConsolided = value.lower() == 'true'

        elif key == 'oneat':
            self.onEat = value

        elif key == 'keepondeplete':
            self.keepOnDeplete = value.lower() == 'true'

        elif key == 'vehicletype':
            self.vehicleType = int(value)

        elif key == 'chancetofall':
            self.chanceToFall = int(value)

        elif key == 'conditionloweroffroad':
            self.conditionLowerOffroad = float(value)

        elif key == 'conditionlowerstandard':
            self.conditionLowerNormal = float(value)

        elif key == 'wheelfriction':
            self.wheelFriction = float(value)

        elif key == 'suspensiondamping':
            self.suspensionDamping = float(value)

        elif key == 'suspensioncompression':
            self.suspensionCompression = float(value)

        elif key == 'engineloudness':
            self.engineLoudness = float(value)

        elif key == 'attachmenttype':
            self.attachmentType = value

        elif key == 'makeuptype':
            self.makeUpType = value

        elif key == 'consolidateoption':
            self.consolidateOption = value

        elif key == 'fabrictype':
            self.fabricType = value

        elif key == 'teachedrecipes':
            self.teachedRecipes = ArrayList(value.split(';'))

        elif key == 'mounton':
            self.mountOn = ArrayList(value.split(';'))

        elif key == 'parttype':
            self.partType = value

        elif key == 'clothingitem':
            self.ClothingItem = value

        elif key == 'evolvedrecipe':
            pass #TODO: NO FIELD TO SET. ADD CUSTOM BLOCK

        elif key == 'staticmodel':
            self.staticModel = value

        elif key == 'primaryanimmask':
            self.primaryAnimMask = value

        elif key == 'secondaryanimmask':
            self.secondaryAnimMask = value

        elif key == 'primaryanimmaskattachment':
            self.primaryAnimMaskAttachment = value

        elif key == 'secondaryanimmaskattachment':
            self.secondaryAnimMaskAttachment = value

        elif key == 'replaceinsecondhand':
            self.replaceInSecondHand = value

        elif key == 'replaceinprimaryhand':
            self.replaceInPrimaryHand = value

        elif key == 'replacewhenunequip':
            self.replaceWhenUnequip = value

        elif key == 'eattype':
            self.eatType = value

        elif key == 'iconsfortexture':
            self.IconsForTexture = ArrayList(value.split(';'))

        elif key == 'bloodlocation':
            self.bloodClothingType = ArrayList(value.split(';'))

        elif key == 'obsolete':
            self.OBSOLETE = value.lower() == 'true'


        else:
            logger.debug("adding unknown item param \%s = \%s", key, value)
            # TODO: get LuaManager and DefaultModData

