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
  for 

  return %{@2}

%%
  @0 = #[
    1 2 3
  ]#;
  @1 = #[
    4 5 6
  ]#;
%%

print(add(%{@0}, %{@1}))
```