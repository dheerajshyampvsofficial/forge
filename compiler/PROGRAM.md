`Program`
- Data
- Instructions

`Instructions`
- `Sections`
  - `Section 1`: [insts...]
  - `Sections 2`: [insts...]

`Data`
- Variables (global)
- Format: `Cells` ([ | | | ....], sliced via index like @0, @1, ....)

`FDS code structure`

- `%% ... %%` -> Section in the `Program`, transpiled as self.interpreter.run_section(idx) 
- `%{ ... }` -> eval() # Please help how to store
- `$$` -> Inline foreign code block
- `${}`-> Inline foreign code expression

`Examples`

```fds
def add(a, b):
  %%
    @0 = {{a}};
    @b = {{b}};
    @2 = @0 + @2;
  %%

  return %{@2}

a = %{
  #[
    1 2 3
    4 5 6
  ]#
}
print(add(3, 3))
```