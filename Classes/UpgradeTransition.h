//
//  UpgradeTransition.h
//  MonkeySwipe
//
//  Created by johan ten broeke on 3/29/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "WinTransition.h"


@interface UpgradeTransition :WinTransition{
	UIActivityIndicatorView *ai;
	BOOL busyUpgrading;
}
-(void) showActivityIndicator;
-(void) hideActivityIndicator;
@end
