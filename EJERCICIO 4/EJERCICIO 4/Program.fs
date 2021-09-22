// Learn more about F# at http://fsharp.org

open System

[<EntryPoint>]
let main argv =
    
    let verificarPares num = (num % 2) = 0

    let verificarImpares num = verificarPares num = false

    let listaDeNumeros = [|1;2;3;4;5;6;7;8;9;10|]

    let listaDePares[] = Seq.where (fun num -> verificarPares num) listaDeNumeros
    let listaDeImpares[] = Seq.where (fun num -> verificarImpares num) listaDeNumeros
    
    Console.Write("lista de pares: ")
    Console.Write("[ ")
    for i in listaDePares[] do
        //printfn "%i" i
        Console.Write(i.ToString() + " ")

    Console.Write("]")

    Console.Write("\n")

    Console.Write("lista de impares: ")
    Console.Write("[ ")
    for i in listaDeImpares[] do
        //printfn "%i" i
        Console.Write(i.ToString() + " ")

    Console.Write("]")

    Console.ReadKey() |>ignore
    0