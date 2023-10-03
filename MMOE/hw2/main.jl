using Plots

function f(x)
    return exp(-x^2)
end

function simpson(a, b, n)
    # a, b: the interval of integration
    h = (b - a) / n
    x = LinRange(a, b, n + 1)
    y = f.(x)
    s = y[1] + y[end]
    for i in 2:2:n
        s += 4 * y[i]
    end
    for i in 3:2:n - 1
        s += 2 * y[i]
    end
    return s * h / 3
end

function main()
    # get input
    println("Input a, b, n:")
    a = parse(Float64, readline())
    b = parse(Float64, readline())
    n = parse(Int, readline())
    println("Result: ", simpson(a, b, n))

end

main()