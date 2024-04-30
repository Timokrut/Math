import shutil
import os

def clear_and_write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def create_template_files(template_folder):
    template_contents = {
        'geogebra_thumbnail.png': '',  
        
        'geogebra_javascript.js': 'function ggbOnInit() {}',  

        'geogebra_defaults3d.xml': 
        '''<geogebra xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" format="5.0" version="5.2.832.0" app="3d" platform="w" xsi:noNamespaceSchemaLocation="http://www.geogebra.org/apps/xsd/ggt.xsd">
            <defaults>
            <element type="conic3d" label="Intersection curve" default="3150">
            <coords ox="0" oy="0" oz="0" ow="1" vx="0" vy="0" vz="0" wx="0" wy="0" wz="0"/>
            <show object="true" label="true"/>
            <objColor r="21" g="101" b="192" alpha="0.10000000149011612"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="0.1" speed="1" type="0" playing="false"/>
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <eqnStyle style="parametric"/>
            <eigenvectors x0="1" y0="0" z0="1.0" x1="0" y1="1" z1="1.0"/>
            <matrix A0="0" A1="0" A2="0" A3="0" A4="0" A5="0"/>
            </element>
            <element type="axis3D" label="Axis3D" default="3103">
            <show object="true" label="true"/>
            <objColor r="0" g="0" b="0" alpha="0"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="0.1" speed="1" type="0" playing="false"/>
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <eqnStyle style="parametric" parameter="λ"/>
            </element>
            <element type="curvecartesian3d" label="Curve3D" default="3106">
            <show object="true" label="true"/>
            <objColor r="0" g="0" b="0" alpha="0"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="1" speed="1" type="0" playing="false"/>
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            </element>
            <element type="plane3d" label="Plane3D" default="3200">
            <show object="true" label="true"/>
            <objColor r="99" g="219" b="219" alpha="0.5"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <fading val="0.10000000149011612"/>
            <lineStyle thickness="0" type="0" typeHidden="1"/>
            <coords x="0" y="0" z="0" w="0"/>
            </element>
            <element type="polyhedron" label="Polyhedron" default="3300">
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <show object="true" label="true"/>
            <objColor r="21" g="101" b="192" alpha="0.4000000059604645"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="1" speed="1" type="0" playing="false"/>
            </element>
            <element type="polyhedron" label="Archimedean" default="3312">
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <show object="true" label="true"/>
            <objColor r="211" g="47" b="47" alpha="0.4000000059604645"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="1" speed="1" type="0" playing="false"/>
            </element>
            <element type="polyhedron" label="Pyramid" default="3310">
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <show object="true" label="true"/>
            <objColor r="219" g="97" b="20" alpha="0.4000000059604645"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="1" speed="1" type="0" playing="false"/>
            </element>
            <element type="polyhedron" label="Prism" default="3311">
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <show object="true" label="true"/>
            <objColor r="216" g="27" b="96" alpha="0.4000000059604645"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="1" speed="1" type="0" playing="false"/>
            </element>
            <element type="net" label="Net" default="3305">
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <show object="true" label="true"/>
            <objColor r="21" g="101" b="192" alpha="0.4000000059604645"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <animation step="1" speed="1" type="0" playing="false"/>
            </element>
            <element type="quadric" label="Quadric" default="3301">
            <show object="true" label="true"/>
            <objColor r="211" g="47" b="47" alpha="0.6499999761581421"/>
            <layer val="0"/>
            <autocolor val="false"/>
            <labelMode val="4"/>
            <lineStyle thickness="5" type="0" typeHidden="1"/>
            <eqnStyle style="implicit"/>
            <eigenvectors x0="1" y0="0" z0="0" x1="0" y1="1" z1="0" x2="0" y2="0" z2="1"/>
            <matrix A0="0" A1="0" A2="0" A3="0" A4="0" A5="0" A6="0" A7="0" A8="0" A9="0"/>
            </element>
            <element type="surfacecartesian3d" label="surface" default="3304">
            <show object="true" label="true"/>
            <objColor r="204" g="0" b="0" alpha="0.75"/>
            <layer val="0"/>
            <autocolor val="true"/>
            <labelMode val="4"/>
            <animation step="1" speed="1" type="0" playing="false"/>
            <lineStyle thickness="1" type="0" typeHidden="1"/>
            </element>
            </defaults>
            </geogebra>
        ''',  

        'geogebra_defaults2d.xml': 

        '''<geogebra xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" format="5.0" version="5.2.832.0" app="3d" platform="w" xsi:noNamespaceSchemaLocation="http://www.geogebra.org/apps/xsd/ggt.xsd">
        <defaults>
        <element type="point" label="Point (free)" default="10">
        <show object="true" label="true"/>
        <objColor r="21" g="101" b="192" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="0.1" speed="1" type="1" playing="false"/>
        <pointSize val="5"/>
        <pointStyle val="0"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="point" label="Point (dependent)" default="11">
        <show object="true" label="true"/>
        <objColor r="97" g="97" b="97" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="0.1" speed="1" type="1" playing="false"/>
        <pointSize val="4"/>
        <pointStyle val="0"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="point" label="Point (dependent)" default="16">
        <show object="true" label="true"/>
        <objColor r="97" g="97" b="97" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="1" playing="false"/>
        <pointSize val="4"/>
        <pointStyle val="10"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="point" label="PointOn" default="12">
        <show object="true" label="true"/>
        <objColor r="21" g="101" b="192" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="1" playing="false"/>
        <pointSize val="5"/>
        <pointStyle val="0"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="point" label="PointInRegion" default="13">
        <show object="true" label="true"/>
        <objColor r="21" g="101" b="192" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="1" playing="false"/>
        <pointSize val="5"/>
        <pointStyle val="0"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="point" label="PointOn" default="14">
        <show object="true" label="true"/>
        <objColor r="21" g="101" b="192" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="1" playing="false"/>
        <coordStyle style="complex"/>
        <pointSize val="5"/>
        <pointStyle val="0"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="line" label="Line" default="20">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="0.1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        <eqnStyle style="implicit"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="function" label="Curve" default="3400">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="true"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        </element>
        <element type="segment" label="Segment" default="21">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="0.1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        <eqnStyle style="explicit"/>
        <outlyingIntersections val="false"/>
        <keepTypeOnTransform val="true"/>
        <startStyle val="default"/>
        <endStyle val="default"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="ray" label="Segment" default="25">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        <eqnStyle style="explicit"/>
        <outlyingIntersections val="false"/>
        <keepTypeOnTransform val="true"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="functionnvar" label="" default="23">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="255" alpha="0.25"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        </element>
        <element type="function" label="" default="24">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1"/>
        </element>
        <element type="functionnvar" label="" default="65">
        <show object="true" label="true"/>
        <objColor r="204" g="0" b="0" alpha="0.75"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        </element>
        <element type="vector" label="Vector" default="30">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        <coordStyle style="cartesian"/>
        <coords x="NaN" y="NaN" z="NaN"/>
        </element>
        <element type="polygon" label="Polygon" default="70">
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="204"/>
        <show object="true" label="false"/>
        <objColor r="21" g="101" b="192" alpha="0.10000000149011612"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="0.1" speed="1" type="0" playing="false"/>
        </element>
        <element type="polyline" label="Polyline" default="71">
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="0.1" speed="1" type="0" playing="false"/>
        </element>
        <element type="conic" label="Conic" default="40">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        <eqnStyle style="implicit"/>
        <eigenvectors x0="1" y0="0" z0="1.0" x1="0" y1="1" z1="1.0"/>
        <matrix A0="0" A1="0" A2="0" A3="0" A4="0" A5="0"/>
        </element>
        <element type="conicpart" label="Sector" default="41">
        <show object="true" label="true"/>
        <objColor r="21" g="101" b="192" alpha="0.10000000149011612"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="204"/>
        <eqnStyle style="implicit"/>
        <outlyingIntersections val="false"/>
        <keepTypeOnTransform val="true"/>
        <eigenvectors x0="1" y0="0" z0="1.0" x1="0" y1="1" z1="1.0"/>
        <matrix A0="0" A1="0" A2="0" A3="0" A4="0" A5="0"/>
        </element>
        <element type="numeric" label="Numeric" default="50">
        <value val="0"/>
        <slider min="-5" max="5" absoluteScreenLocation="true" width="200" fixed="false" horizontal="true" showAlgebra="true"/>
        <lineStyle thickness="2" type="0" typeHidden="1"/>
        <objColor r="0" g="0" b="0" alpha="0.10000000149011612"/>
        <autocolor val="false"/>
        <animation speed="1" type="0" playing="false"/>
        </element>
        <element type="angle" label="Angle" default="52">
        <angleStyle val="0"/>
        <value val="0"/>
        <slider min="0" max="6.283185307179586" absoluteScreenLocation="true" width="180" fixed="true" horizontal="true" showAlgebra="true"/>
        <lineStyle thickness="5" type="0" typeHidden="2" opacity="153"/>
        <arcSize val="30"/>
        <objColor r="0" g="0" b="0" alpha="0.10000000149011612"/>
        <autocolor val="false"/>
        <animation step="0.017453292519943295" speed="1" type="0" playing="false"/>
        </element>
        <element type="function" label="Function" default="60">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="true"/>
        <labelMode val="4"/>
        <fixed val="true"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        </element>
        <element type="locus" label="Locus" default="80">
        <show object="true" label="false"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        <auxiliary val="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="178"/>
        </element>
        <element type="text" label="Text" default="100">
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        </element>
        <element type="image" label="Image" default="110">
        <file name=""/>
        <inBackground val="false"/>
        <show object="true" label="true"/>
        <objColor r="0" g="0" b="0" alpha="1"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="1" speed="1" type="0" playing="false"/>
        </element>
        <element type="boolean" label="Boolean" default="120">
        <value val="false"/>
        <show object="false" label="true"/>
        <objColor r="28" g="28" b="31" alpha="0"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <checkbox fixed="true"/>
        </element>
        <element type="list" label="List" default="130">
        <show object="false" label="true"/>
        <objColor r="0" g="100" b="0" alpha="-1"/>
        <layer val="0"/>
        <autocolor val="false"/>
        <labelMode val="4"/>
        <animation step="0.1" speed="1" type="0" playing="false"/>
        <lineStyle thickness="5" type="0" typeHidden="1"/>
        <pointSize val="5"/>
        <pointStyle val="0"/>
        <angleStyle val="0"/>
        </element>
        </defaults>
        </geogebra>
        ''',  

        'geogebra.xml': 
        '''<geogebra xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" format="5.0" version="5.2.832.0" app="3d" platform="w" id="ba372b8c-cfd3-4a8c-b392-be1fb19a8c15" xsi:noNamespaceSchemaLocation="http://www.geogebra.org/apps/xsd/ggb.xsd">
        <gui>
        <window width="1488" height="678"/>
        <perspectives>
        <perspective id="tmp">
        <panes>
        <pane location="" divider="0.260752688172043" orientation="1"/>
        </panes>
        <views>
        <view id="4097" visible="false" inframe="false" stylebar="true" location="1,1,1,1" size="400" window="100,100,700,550"/>
        <view id="8" toolbar="1001 | 1002 | 1003 || 1005 | 1004 || 1006 | 1007 | 1010 || 1008 | 1009 || 6" visible="false" inframe="false" stylebar="false" location="1,3,3" size="300" window="100,100,600,400"/>
        <view id="1" visible="false" inframe="false" stylebar="false" location="1,3" size="500" window="100,100,600,400"/>
        <view id="4" toolbar="0 || 2020 , 2021 , 2022 || 2001 , 2003 , 2002 , 2004 , 2005 || 2040 , 2041 , 2042 , 2044 , 2043" visible="false" inframe="false" stylebar="false" location="1,1" size="300" window="100,100,600,400"/>
        <view id="2" visible="true" inframe="false" stylebar="false" location="3" size="388" tab="TOOLS" window="100,100,250,400"/>
        <view id="16" visible="false" inframe="false" stylebar="false" location="1" size="300" window="50,50,500,500"/>
        <view id="32" visible="false" inframe="false" stylebar="true" location="1" size="300" window="50,50,500,500"/>
        <view id="64" toolbar="0" visible="false" inframe="false" stylebar="false" location="1" size="480" window="50,50,500,500"/>
        <view id="128" visible="false" inframe="false" stylebar="false" location="1" size="480" window="50,50,500,500"/>
        <view id="70" toolbar="0 || 2020 || 2021 || 2022" visible="false" inframe="false" stylebar="true" location="1" size="900" window="50,50,500,500"/>
        <view id="512" toolbar="0 | 1 501 5 19 , 67 | 2 15 45 18 , 7 37 | 514 3 9 , 13 44 , 47 | 16 51 | 551 550 11 , 20 22 21 23 , 55 56 57 , 12 | 69 | 510 511 , 512 513 | 533 531 , 534 532 , 522 523 , 537 536 , 535 , 538 | 521 520 | 36 , 38 49 560 | 571 30 29 570 31 33 | 17 | 540 40 41 42 , 27 28 35 , 6 , 502" visible="true" inframe="false" stylebar="false" location="1" size="1084" window="100,100,600,400"/>
        </views>
        <toolbar show="true" items="0 77 73 62 | 1 501 67 , 5 19 , 72 75 76 | 2 15 45 , 18 65 , 7 37 | 4 3 8 9 , 13 44 , 58 , 47 | 16 51 64 , 70 | 10 34 53 11 , 24 20 22 , 21 23 | 55 56 57 , 12 | 36 46 , 38 49 50 , 71 14 68 | 30 29 54 32 31 33 | 25 17 26 60 52 61 | 40 41 42 , 27 28 35 , 6" position="1" help="false"/>
        <input show="true" cmd="true" top="algebra"/>
        <dockBar show="false" east="false"/>
        </perspective>
        </perspectives>
        <labelingStyle val="0"/>
        <font size="16"/>
        </gui>
        <euclidianView>
        <viewNumber viewNo="1"/>
        <coordSystem xZero="0" yZero="0" scale="50" yscale="50"/>
        <evSettings axes="true" grid="false" gridIsBold="false" pointCapturing="3" rightAngleStyle="1" checkboxSize="26" gridType="3"/>
        <bgColor r="255" g="255" b="255"/>
        <axesColor r="37" g="37" b="37"/>
        <gridColor r="192" g="192" b="192"/>
        <lineStyle axes="1" grid="0"/>
        <axis id="0" show="true" label="" unitLabel="" tickStyle="1" showNumbers="true"/>
        <axis id="1" show="true" label="" unitLabel="" tickStyle="1" showNumbers="true"/>
        </euclidianView>
        <algebraView>
        <mode val="3"/>
        </algebraView>
        <kernel>
        <uses3D val="true"/>
        <continuous val="false"/>
        <usePathAndRegionParameters val="true"/>
        <decimals val="2"/>
        <angleUnit val="degree"/>
        <algebraStyle val="3" spreadsheet="0"/>
        <coordStyle val="0"/>
        </kernel>
        <tableview min="0" max="0" step="0"/>
        <scripting blocked="false" disabled="false"/>
        <euclidianView3D>
        <coordSystem xZero="-1.6592442862691277" yZero="-0.38480420944391364" zZero="-0.6726237226067859" scale="137.36162060049543" xAngle="23" zAngle="50"/>
        <evSettings axes="false" grid="false" gridIsBold="false" pointCapturing="3" rightAngleStyle="1" gridType="3"/>
        <axis id="0" show="false" label="x" unitLabel="" tickStyle="1" showNumbers="true"/>
        <axis id="1" show="false" label="y" unitLabel="" tickStyle="1" showNumbers="true"/>
        <axis id="2" show="false" label="z" unitLabel="" tickStyle="1" showNumbers="true"/>
        <plate show="false"/>
        <bgColor r="255" g="255" b="255"/>
        <clipping use="false" show="false" size="1"/>
        <projection type="0"/>
        </euclidianView3D>
        <construction title="Your figure" author="" date="">
        '''  
    }

    for file_name, content in template_contents.items():
        file_path = os.path.join(template_folder, file_name)
        clear_and_write_file(file_path, content)

def create_template(path):
    template_folder = os.path.join(path, 'ggb_template')
    try:
        os.makedirs(template_folder)
    except OSError:
        pass

    create_template_files(template_folder)

def create_ggb_file(source_folder, target_rar):
    shutil.make_archive(target_rar, 'zip', source_folder)
    os.rename(target_rar + '.zip', target_rar)

def read_obj_file(file_path):
    vertices = []
    faces = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertices.append([float(x) for x in line.strip().split()[1:]])
            elif line.startswith('f '):
                faces.append([int(x.split('/')[0]) for x in line.strip().split()[1:]])
    return vertices, faces

def add_point(point_name: str, coordinates: list[float]) -> None:
    content = f'''
        <expression label="{point_name}" exp="({coordinates[0]}, {coordinates[1]}, {coordinates[2]})" type="point"/> 
            <element type="point3d" label="{point_name}">
                <show object="true" label="false" ev="20"/>
                <objColor r="0" g="0" b="0" alpha="0"/>
                <layer val="0"/>
                <labelMode val="0"/>
                <fixed val="true"/>
                <pointSize val="5"/>
                <coords x="{coordinates[0]}" y="{coordinates[1]}" z="{coordinates[2]}" w="1"/>
            </element>  
        '''
    with open('./ggb_template/ggb_template/geogebra.xml', 'a') as file:
        file.write(content)
    
    #t1 = Polygon(point, ..., point)
    #       ↑--------n--------↑
    #Creates n Segments
    #v0 = Segment(point2, point3, t1)
    #v1 = Segment(point3, point0, t1)
    #v2 = Segment(point0, point2, t1)
    
def create_polygon(faces: list[int]):
    if not hasattr(create_polygon, "counter"):
        create_polygon.counter = 0
    create_polygon.counter += 1

    content = f'''<command name="Polygon">
        <input a0="V{faces[0] - 1}" a1="V{faces[1] - 1}" a2="V{faces[2] - 1}"/>
        <output a0="t{create_polygon.counter}" a1="v{faces[2] - 1}" a2="v{faces[1] - 1}" a3="v{faces[0] - 1}"/>
    </command>
    <element type="polygon3d" label="t{create_polygon.counter}">
        <lineStyle thickness="5" type="0" typeHidden="1" opacity="204"/>
        <show object="true" label="false" ev="4"/>
        <objColor r="21" g="101" b="192" alpha="1"/>
        <layer val="0"/>
        <labelMode val="0"/>
    </element>
    <element type="segment3d" label="v{faces[2] - 1}">
        <show object="true" label="false" ev="4"/>
        <objColor r="21" g="101" b="192" alpha="0"/>
        <layer val="0"/>
        <labelMode val="0"/>
        <auxiliary val="false"/>
        <lineStyle thickness="0" type="0" typeHidden="1"/>
        <outlyingIntersections val="false"/>
        <keepTypeOnTransform val="true"/>
    </element>
        <element type="segment3d" label="v{faces[1] - 1}">
        <show object="true" label="false" ev="4"/>
        <objColor r="21" g="101" b="192" alpha="0"/>
        <layer val="0"/>
        <labelMode val="0"/>
        <auxiliary val="false"/>
        <lineStyle thickness="0" type="0" typeHidden="1"/>
        <outlyingIntersections val="false"/>
        <keepTypeOnTransform val="true"/>
    </element>
    <element type="segment3d" label="v{faces[0] - 1}">
        <show object="true" label="false" ev="4"/>
        <objColor r="21" g="101" b="192" alpha="0"/>
        <layer val="0"/>
        <labelMode val="0"/>
        <auxiliary val="false"/>
        <lineStyle thickness="0" type="0" typeHidden="1"/>
        <outlyingIntersections val="false"/>
        <keepTypeOnTransform val="true"/>
    </element>'''

    with open('./ggb_template/ggb_template/geogebra.xml', 'a') as file:
        file.write(content)

if __name__ == "__main__":
    create_template("ggb_template")
    
    verticies, faces = read_obj_file('./model.obj')

    for number, point in enumerate(verticies):
        name = f'V{number}'
        add_point(name, point)
    
    for face in faces:
        create_polygon(face)

    endfile = '''</construction>
            </geogebra>'''
    with open ('./ggb_template/ggb_template/geogebra.xml', 'a') as file:
        file.write(endfile)
    #create .ggb    
    source_folder = './ggb_template/ggb_template'
    target_rar = 'figure.ggb'
    create_ggb_file(source_folder, target_rar)