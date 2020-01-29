if "bpy" not in locals():
    import bpy
    from . import receiver
    from . import animations
    from . import animation_lists
    from . import utils
    from . import state_manager
    from . import icon_manager
    from . import recorder
else:
    import importlib

    importlib.reload(receiver)
    importlib.reload(animations)
    importlib.reload(animation_lists)
    importlib.reload(utils)
    importlib.reload(state_manager)
    importlib.reload(icon_manager)
    importlib.reload(recorder)