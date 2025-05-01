# APWorld integration

This document describes the changes you need to make to fully integrate your APWorld with Universal Tracker. It assumes you are already familiar with the basics of how UT works. If you haven't already, read through the [re-gen-passthrough](re-gen-passthrough.md) document.

## Providing information during generation

UT does not have access to the seed used during the original generation. This means that any randomization that is not a direct result of YAML options or AP items will not be the same when UT runs and must be provided in slot data. This can include entrance rando (GER or otherwise), level order, starting location, or any similar options that don't use items directly.

Best practice is to store these random results on your world instance and pass them into the result of `fill_slot_data`.

```python
    def fill_slot_data(self) -> dict[str, Any]:
        return {
            "starting_location": self.starting_location,
            "entrances": self.randomized_entrances,
            # etc
        }
```

## Loading provided information

```python
    def interpret_slot_data(self, slot_data: dict[str, Any]) -> None:
        if "starting_location" in slot_data:
            self.starting_location = slot_data["starting_location"]
        if "entrances" in slot_data:
            for entrance in slot_data["entrances"]:
                # you may need to adjust region connections for
```

```python
    def create_regions(self) -> None:
        is_ut = getattr(self, "generation_is_fake", False)
        if self.option.randomize_things.value or is_ut:
            self.create_location(...)
```

## Generating without a YAML

```python
    def fill_slot_data(self) -> dict[str, Any]:
        option_fields = [field.name for field in dataclasses.fields(self.options)]
        # to exclude default options you can add:
        # if field not in dataclasses.fields(PerGameCommonOptions)
        return {
            # randomized results as above
            "options": self.options.as_dict(*option_fields),
        }
```

```python
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a 2nd generation in UT
        return slot_data
```

```python
    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Optional[Option] = getattr(self.options, key, None)
                if opt is not None:
                    # You can also set .value directly but that won't work if you have OptionSets
                    setattr(self.options, key, opt.from_any(value))
```

The last thing to do is inform UT that your world can generate without a YAML.

```python
class MyWorld(World):
    ut_can_gen_without_yaml = True
```
