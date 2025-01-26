using Images, ImageIO
using FileIO
using GLMakie; GLMakie.activate!()


# Load Noise image
img = load("noise.png")[1:2250, 1:1000 ];  # make sure to use the correct path to your image file
new(x, newval, originalval) = newval * x / originalval
newr(x) = new(x, 0.23, 0.15)
newg(x) = new(x, 0.6, 0.15)
newb(x) = new(x, 0.67, 0.15)

image(img)
image(fill(RGB(0.2, 0.2, 0.2), 2, 2))



# vals = Float64[];
begin
    newimg = Matrix{RGBA}(undef, size(img));
    for row in axes(img,1)
        for col in axes(img,2)
            (;r,g,b) = img[row,col];
            r, g, b = newr(r),newg(g), newb(b) 
            # [push!(vals, chan) for chan in [r,g,b]]
            newimg[row, col] = RGBA(r/4,g/4, b/4, 0.5)
            # newimg[row, col] = all([r,g,b] .> 0.6) ? RGB(r*1.2,g*1.5,b*1.5) : RGB(0.23, 0.6, .67)
        end
    end
    
    # Reverse otherwise the flaw will go up
    revimg = reverse(newimg)
end;


image(newimg)

# Create textures
image_height = 500
whindow_height = 50
i = 0
while image_height + i*whindow_height < size(revimg,1)
    framename = "$i.png"
    start, stop = 1 + i*whindow_height, image_height + i*whindow_height
    save(framename, revimg[start:stop, 1:200])
    i += 1
end



# Load your image
img = load("template.jpeg")[1:1200, 1:500];  # make sure to use the correct path to your image file

begin
    newimg = Matrix{RGB}(undef, size(img));
    for row in axes(img,1)
        for col in axes(img,2)
            (;r,g,b) = img[row,col];
            newimg[row, col] = all([r,g,b] .> 0.5) ? RGB(r,g,b) : RGB(0.23, 0.6, .67)
        end
    end
    
    # Reverse otherwise the flaw will go up
    newimg = reverse(newimg, dims=1)
end;

# Create textures
image_height = 500
whindow_height = 50
i = 0
while image_height + i*whindow_height < size(newimg,1)
    framename = "$i.png"
    start, stop = 1 + i*whindow_height, image_height + i*whindow_height
    save(framename, newimg[start:stop, 1:image_height])
    i += 1
end


# Look at images ---
f = Figure(resolution=size(newimg'))
image(f[1,1],newimg')

f = Figure(resolution=size( vcat(newimg, newimg) ) )
image(f[1,1], vcat(reverse(newimg, dims=1), newimg))

reverse(newimg, dims=1)

image(rotr90(img), axis = (aspect = DataAspect()))


