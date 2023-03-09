XAUTH=/tmp/.docker.xauth

echo "Preparing Xauthority data..."
xauth_list=$(xauth nlist :0 | tail -n 1 | sed -e 's/^..../ffff/')
if [ ! -f $XAUTH ]; then
    if [ ! -z "$xauth_list" ]; then
        echo $xauth_list | xauth -f $XAUTH nmerge -
    else
        touch $XAUTH
    fi
    chmod a+r $XAUTH
fi

docker compose build
docker compose run crazyflie python3 ./safe-control-gym/examples/3d_quad.py --overrides ./safe-control-gym/examples/3d_quad.yaml
docker compose run crazyflie python3 ./safe-control-gym/examples/tracking.py --overrides ./safe-control-gym/examples/tracking.yaml
docker compose down