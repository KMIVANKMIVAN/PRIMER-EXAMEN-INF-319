// Learn more about F# at http://fsharp.org

open System

[<EntryPoint>]
let main argv =

    let multiplicar m n =
        let mutable acumulador = 0
        for i = 1 to n do
            acumulador <- acumulador + m
        acumulador

    multiplicar 5 10 
    |> printfn "la multiplicacion es: %d"

    Console.ReadKey() |>ignore
    0 // return an integer exit code
