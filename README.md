# nix-wpe-webkit

Standalone `wpewebkit` package for Nix, with optional binary cache publishing via Cachix.

## Build locally

```bash
nix build .#wpewebkit
```

## Use as a flake input

```nix
{
  inputs.nix-wpe-webkit.url = "github:eval-exec/nix-wpe-webkit";

  outputs = { self, nixpkgs, nix-wpe-webkit, ... }: {
    nixosConfigurations.myhost = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        ({ pkgs, ... }: {
          nixpkgs.overlays = [ nix-wpe-webkit.overlays.default ];
          environment.systemPackages = [ pkgs.wpewebkit ];
        })
      ];
    };
  };
}
```

## Binary cache (Cachix)

1. Create a cache at https://app.cachix.org.
2. In GitHub repo settings, add:
   - Secret: `CACHIX_AUTH_TOKEN` (write token from Cachix).
   - Variable: `CACHIX_CACHE_NAME` (your cache name, for example `nix-wpe-webkit`).
3. Push to `main` to trigger `.github/workflows/ci.yml`.

Users can enable your cache with:

```bash
cachix use <your-cache-name>
```

Then build/install normally:

```bash
nix build github:eval-exec/nix-wpe-webkit#wpewebkit
```

If the exact derivation is already built in your cache, users download binaries instead of building locally.
