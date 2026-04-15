{
  description = "Standalone WPE WebKit package for Nix";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
  };

  outputs = {nixpkgs, ...}: let
    systems = [
      "x86_64-linux"
      "aarch64-linux"
    ];

    overlay = import ./overlay.nix;

    forAllSystems = f:
      nixpkgs.lib.genAttrs systems (
        system:
          f (
            import nixpkgs {
              inherit system;
              overlays = [overlay];
            }
          )
      );
  in {
    overlays.default = overlay;

    packages = forAllSystems (pkgs: {
      wpewebkit = pkgs.wpewebkit;
      default = pkgs.wpewebkit;
    });

    devShells = forAllSystems (pkgs: {
      default = pkgs.mkShell {
        packages = with pkgs; [
          cachix
          nixfmt
        ];
      };
    });

    formatter = forAllSystems (pkgs: pkgs.nixfmt);
  };
}
