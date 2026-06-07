# Workflow

This folder contains reusable workflow systems.

## ForgeFlow

`WORKFLOW/forgeflow/` is imported from [`hamza-xyric/forgeflow`](https://github.com/hamza-xyric/forgeflow).

ForgeFlow assumes it travels as a self-contained folder named `framework/` inside the project that uses it.

To adopt it:

```bash
cp -R WORKFLOW/forgeflow /path/to/your-project/framework
cd /path/to/your-project
cp -R framework/starter/. .
```

Then read:

```text
framework/START-HERE.md
```

For an existing mature project, use the adoption workflow described by ForgeFlow instead of overwriting root guidance.

## Source Tracking

See `FORGEFLOW-SOURCE.md` for the imported commit, license, and update process.
