//
//  OOOStoreView.h
//  oneonone
//
//  Created by johan ten broeke on 3/26/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import <StoreKit/StoreKit.h>
#import "OOOStoreObserver.h"
#import "OOOReachability.h"


@interface OOOStoreView :UIView <SKProductsRequestDelegate> {
	OOOStoreObserver *observer;
	UIAlertView *warnDisabledAlert; 
	SKProductsRequest *pay_request;
	OOOReachability *reachability_obj;
	BOOL isTrusted;
}

- (void) requestProductData;
@end