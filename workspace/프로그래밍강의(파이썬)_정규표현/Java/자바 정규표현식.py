# Java로 정규 표현식을 다룰 때에는 Pattern 클래스와 Matcher 클래스를 이용합니다.
#
# 주의할 점: Java에서는 \ 대신 \\를 적어야 합니다.
#
# Python은 raw string을 지원해 대표 문자1를 표현할 때 역슬래시 \ 를 한 번만 쓸 수 있습니다.
# 허나, 자바에서는 escape 때문에 역슬래시를 사용해 역슬래시 \를 두 번 적어야 합니다.

# \d, \w 등

import java.io.Console;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class MyRegex{
    public static void main(String[] args){
        String searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\n다스베이더 070-9999-9999 darth_vader@gmail.com\nprincess leia 010 2454 3457 leia@gmail.com";

        Pattern pattern = Pattern.compile("
\\w
");
        Matcher matcher = pattern.matcher(searchTarget);
        while(matcher.find()){
            System.out.println(matcher.group(0));
        }
    }
}