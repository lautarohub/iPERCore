

def create_trainer(name, *args, **kwargs):
    trainer = None

    if name == "LWGTrainer":
        from .lwg_trainer import LWGTrainer
        trainer = LWGTrainer(*args, **kwargs)

    elif name == "LWGAugBGTrainer":
        from .lwg_trainer import LWGAugBGTrainer
        trainer = LWGAugBGTrainer(*args, **kwargs)

    elif name == "LWGFrontTrainer":
        from .lwg_trainer import LWGFrontTrainer
        trainer = LWGFrontTrainer(*args, **kwargs)

    else:
        raise ValueError("Trainer %s not recognized." % name)

    return trainer
